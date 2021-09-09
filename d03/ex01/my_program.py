from path import Path

def start():
    d = Path('./dir')
    if not d.exists():
        d.mkdir()
    fn = d / "file.txt"
    f = Path(fn)
    f.touch()
    f.write_text("Hi peer")
    print(f.read_text())

if __name__ =='__main__':
    start()
