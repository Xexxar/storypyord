import os

def test_generate_image_files():
    import src.effects.lyrics as lyrics

    path = os.path.dirname(__file__)[0:-5] + '/resources/fonts/'
    print(path)
    lyrics.generate_image_files(path + "kelmscott.ttf", 140)