"""CRT SOURCE-NOTE PIPELINE (charter-owned, lives only under crt/).

Purpose: ingest teacher videos atяр маximum available resolution with the
user-ratified fidelity bar (Amendment A1):
  Pass A  global dense sweep    - 1 fps contact sheets (12-tile 3x4, ts burned)
  Pass B  transcript            - full VTT (auto-captions) -> readable plain text
  Pass C  full-res event pulls  - scene-cut driven + targeted segments, 4K frames
  Pass D  re-verification       - (done by the agent, recorded in notes)
Per-video MODE stamp recorded. Temp video deleted after extraction (storage
rule); only KB-scale notes + sheet jpgs persist under crt/notes/.

Usage:
  python video_pipeline.py list                          # (handled by yt-dlp)
  python video_pipeline.py extract ID [--fps 1.0] [--sheets 12] [--res 480]
      [segment spec: --seg t_start-t_end,...]            # full-res re-pulls
  python video_pipeline.py vtt ID
"""
import argparse
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TMP = os.path.join(os.environ.get("TEMP", "/tmp"), "opencode", "crt_video_tmp")
NOTES = os.path.join(HERE, "notes")
FFMPEG = None

try:
    import imageio_ffmpeg
    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    FFMPEG = None


def tmp_path(*parts):
    d = os.path.join(TMP, *parts)
    os.makedirs(d, exist_ok=True)
    return d


def run(cmd, **kw):
    p = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if p.returncode != 0:
        sys.stderr.write(p.stdout[-3000:] + "\n" + p.stderr[-6000:] + "\n")
        raise SystemExit(f"cmd failed: {' '.join(cmd[:4])}...")
    return p.stdout


# ---------------------------------------------------------------- passages

def extract_pass_a(video_file, work, fps=1.0, tiles=12, res=480):
    """1fps tiles -> contact sheets with burned top-left HH:MM:SS timestamp."""
    sheet_dir = tmp_path(work, "sheets")
    n_col = 4 if tiles > 12 else 3
    n_row = tiles // n_col + (1 if tiles % n_col else 0)
    wm = 28
    args = [FFMPEG, "-y", "-i", video_file, "-vf",
            (f"fps={fps},scale={res}:-1,"
             f"drawtext=fontfile='C\\:/Windows/Fonts/arialbd.ttf':"
             f"text='%{{pts\\:hms}}':start_number=0:x=6:y=6:"
             f"fontsize={wm}:fontcolor=navy:box=1:boxcolor=white@0.8:boxborderw=4,"
             f"drawtext=fontfile='C\\:/Windows/Fonts/arialbd.ttf':"
             f"text='%{{pts\\:hms}}':start_number=0:x=6:y={wm+10}:"
             f"fontsize={wm}:fontcolor=orange:box=1:boxcolor=black@0.6:boxborderw=4"
             f",tile={n_col}x{n_row}"),
            "-start_number", "0", os.path.join(sheet_dir, "sheet_%03d.jpg")]
    txt = run(args)
    sys.stderr.write(txt[-800:])
    sheets = sorted(os.listdir(sheet_dir))
    per_sheet = n_col * n_row
    return sheet_dir, sheets, per_sheet, n_row


def scene_cuts(video_file, work, thresh=0.06):
    """ffmpeg scene-change table -> second list (dedup 2s)."""
    out = run([FFMPEG, "-y", "-i", video_file, "-vf",
               f"select='gt(scene,{thresh})',metadata=print:"
               "file=-", "-an", "-f", "null", "-"], timeout=None)
    cuts = []
    for ln in out.splitlines():
        if "pts_time:" in ln:
            t = float(ln.split("pts_time:")[1].split()[0])
            if t > 3.0:
                cuts.append(t)
    res = []
    for t in cuts:
        if not res or t - res[-1] > 2.0:
            res.append(t)
    path = os.path.join(tmp_path(work), "scene_cuts.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(res, f)
    return res


def extract_range(video_file, work, a, b, step=0.5):
    """Full-res frames over [a,b] at `step`, ORIGINAL timestamps burned in
    (-copyts keeps the source clock; -ss fast-seek before -i)."""
    seg_dir = tmp_path(work, "seg")
    vf = (f"fps=1/{step},"
          f"drawtext=fontfile='C\\:/Windows/Fonts/arialbd.ttf':"
          f"text='%{{pts\\:hms}}':x=8:y=8:"
          f"fontsize=40:fontcolor=navy:box=1:boxcolor=white@0.85:boxborderw=6,"
          f"drawtext=fontfile='C\\:/Windows/Fonts/arialbd.ttf':"
          f"text='%{{pts\\:hms}}':x=8:y=54:"
          f"fontsize=40:fontcolor=orange:box=1:boxcolor=black@0.65:boxborderw=6")
    run([FFMPEG, "-y", "-copyts", "-ss", f"{a}", "-to", f"{b}", "-i",
         video_file, "-vf", vf, "-start_number", "0",
         os.path.join(seg_dir, f"r{int(a):05d}_%03d.jpg")], timeout=None)
    return sorted(f for f in os.listdir(seg_dir)
                  if f.startswith(f"r{int(a):05d}_"))


def extract_segment(video_file, work, ts, before=3.0, after=3.0, max_res=None,
                    step=0.5):
    """Full-res frames centered ts at step; scale cap 2160px (quality target)."""
    seg_dir = tmp_path(work, "seg")
    vf = (f"fps=1/{step},"
          f"drawtext=fontfile='C\\:/Windows/Fonts/arialbd.ttf':"
          f"text='%{{pts\\:hms}}':start_number=0:x=8:y=8:"
          f"fontsize=44:fontcolor=navy:box=1:boxcolor=white@0.85:boxborderw=6")
    if max_res:
        vf = f"fps=1/{step},scale={max_res}:-1," + vf.split(",", 1)[1]
    a, b = max(0, ts - before), ts + after
    run([FFMPEG, "-y", "-ss", f"{a}", "-to", f"{b}", "-i", video_file,
         "-vf", vf, "-start_number", "0",
         os.path.join(seg_dir, f"seg_{int(ts * 100):04d}_%03d.jpg")])
    return sorted(f for f in os.listdir(seg_dir)
                  if f.startswith(f"seg_{int(ts * 100):04d}"))


# ---------------------------------------------------------------- captions

def vtt_to_text(vtt):
    out_lines, seen = [], set()
    for ln in vtt.splitlines():
        t = ln.strip()
        if not t or t.startswith(("WEBVTT", "Kind:", "Language:")) or "-->" in t \
                or t[0].isdigit():
            continue
        t = t.replace("\ufeff", "").replace("&nbsp;", " ").strip()
        if t and t not in seen or t == "\ufeff":
            if t not in seen:
                out_lines.append(t)
            seen.add(t)
    return out_lines


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["extract", "cuts", "vttinfo"])
    ap.add_argument("id")
    ap.add_argument("--fps", type=float, default=1.0)
    ap.add_argument("--tiles", type=int, default=12)
    ap.add_argument("--res", type=int, default=480)
    ap.add_argument("--seg", default="")
    ap.add_argument("--thresh", type=float, default=0.06)
    a = ap.parse_args()
    work = a.id
    vd = tmp_path(work)
    files = [f for f in os.listdir(vd) if f.endswith((".webm", ".mkv", ".mp4"))]
    if not files:
        raise SystemExit(f"no video in {vd}")
    vfile = os.path.join(vd, sorted(files)[0])
    if a.action == "extract":
        d, sheets, per, _ = extract_pass_a(vfile, work, a.fps, a.tiles, a.res)
        print(json.dumps({"sheets": len(sheets), "per_sheet": per,
                          "dir": d}))
    elif a.action == "cuts":
        print(json.dumps(scene_cuts(vfile, work, a.thresh)))
    elif a.action == "vttinfo":
        vtts = [f for f in os.listdir(vd) if f.endswith(".vtt")]
        for vtt in vtts:
            lines = vtt_to_text(open(os.path.join(vd, vtt), encoding="utf-8-sig",
                                     errors="replace").read())
            out = os.path.join(vd, vtt.replace(".vtt", ".txt"))
            with open(out, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            print(f"{vtt}: {len(lines)} caption blocks -> {out}")


if __name__ == "__main__":
    main()
