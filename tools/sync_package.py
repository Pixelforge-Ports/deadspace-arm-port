"""Refresh website/package source files. Does not compile or include game data."""
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]
def sync():
    package = ROOT / "package"
    data = package / "deadspace"
    data.mkdir(parents=True, exist_ok=True)
    for name in ["port.json", "README.md", "gameinfo.xml", "cover.png", "screenshot.png"]:
        shutil.copyfile(ROOT / "ports/deadspace" / name, package / name)
    shutil.copyfile(ROOT / "ports/Dead Space.sh", package / "Dead Space.sh")
    for name in ["deadspace.ini", "deadspace.eapx.json", "CREDITS.md", "PUT_DEAD_SPACE_DATA_HERE.txt"]:
        shutil.copyfile(ROOT / "ports/deadspace" / name, data / name)
    shutil.copyfile(ROOT / "tools/eapx.py", data / "eapx.py")
    licenses = data / "licenses"
    licenses.mkdir(exist_ok=True)
    for origin, name in [("LICENSE", "LICENSE-portmaster-port.txt"), ("LICENSE", "LICENSE-eapx.txt"),
                         ("NOTICE.md", "NOTICE.md"), ("ports/deadspace/LICENSE-gptokeyb.txt", "LICENSE-gptokeyb.txt")]:
        shutil.copyfile(ROOT / origin, licenses / name)
    shutil.copyfile(ROOT / "testing_thread.txt", package / "testing_thread.txt")
    shutil.copyfile(ROOT / 'LICENSE', licenses / 'LICENSE-portmaster-port.txt')
    shutil.copyfile(ROOT / 'LICENSE', licenses / 'LICENSE-eapx.txt')
    shutil.copyfile(ROOT / 'NOTICE.md', licenses / 'NOTICE.md')
    shutil.copyfile(ROOT / 'third_party/gmloader/LICENSE.md', licenses / 'LICENSE-gmloader.md')
    shutil.copyfile(ROOT / 'third_party/deadspace-vita/LICENSE', licenses / 'LICENSE-deadspace-vita.txt')
    shutil.copyfile(ROOT / 'third_party/powervr/LICENSE.md', licenses / 'LICENSE-powervr.txt')
    shutil.copyfile(ROOT / 'third_party/vfpvector/LICENSE', licenses / 'LICENSE-vfpvector.txt')
if __name__ == "__main__":
    sync()
    print("Updated package/ website metadata and redistributable source files.")
