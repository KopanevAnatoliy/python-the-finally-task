import pytest

from main import word_counter


def test_standard():
    text = 'Hello world. Hello Python. Hello again.'
    assert word_counter(text) == [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]


def test_ru_locale():
    text = """Равным образом постоянный количественный рост и сфера нашей активности играет важную роль в 
    формировании системы обучения кадров, соответствует насущным потребностям. Товарищи! сложившаяся структура 
    организации представляет собой интересный эксперимент проверки направлений прогрессивного развития. Повседневная 
    практика показывает, что укрепление и развитие структуры обеспечивает широкому кругу (специалистов) участие в 
    формировании дальнейших направлений развития. Равным образом консультация с широким активом требуют определения и 
    уточнения модели развития."""
    assert word_counter(text) == [('и', 3), ('развития', 3), ('равным', 2), ('образом', 2), ('в', 2),
                                  ('формировании', 2), ('направлений', 2), ('постоянный', 1), ('количественный', 1),
                                  ('рост', 1)]


def test_long_text():
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
    dolore magna aliqua. Sit amet consectetur adipiscing elit pellentesque habitant morbi. Arcu cursus vitae congue 
    mauris rhoncus aenean vel elit. Bibendum arcu vitae elementum curabitur vitae nunc. Diam sollicitudin tempor id 
    eu nisl nunc mi. Magna etiam tempor orci eu lobortis elementum nibh. Convallis tellus id interdum velit laoreet. 
    Id cursus metus aliquam eleifend mi in. Nunc eget lorem dolor sed viverra ipsum nunc aliquet. Sed faucibus turpis 
    in eu mi bibendum neque egestas. Commodo nulla facilisi nullam vehicula ipsum a arcu cursus. Molestie at 
    elementum eu facilisis sed odio morbi quis commodo. Sagittis eu volutpat odio facilisis mauris sit amet. Faucibus 
    turpis in eu mi bibendum neque. Sit amet venenatis urna cursus. Tortor consequat id porta nibh venenatis cras sed 
    felis eget. Ultrices tincidunt arcu non sodales neque sodales ut etiam sit. Interdum velit laoreet id donec 
    ultrices tincidunt arcu non sodales. Justo laoreet sit amet cursus sit amet dictum sit.

    Sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus. Bibendum est ultricies integer quis auctor elit. 
    Blandit libero volutpat sed cras ornare arcu. Maecenas ultricies mi eget mauris pharetra et ultrices neque ornare. 
    Vel turpis nunc eget lorem dolor sed viverra ipsum nunc. Sed vulputate odio ut enim blandit volutpat maecenas. 
    Aliquam etiam erat velit scelerisque in dictum. Nec ultrices dui sapien eget mi proin. Proin sed libero enim sed 
    faucibus turpis in eu. Diam donec adipiscing tristique risus nec feugiat. Arcu vitae elementum curabitur vitae nunc 
    sed velit dignissim. Risus sed vulputate odio ut enim blandit volutpat maecenas.
    
    Lorem mollis aliquam ut porttitor. Et pharetra pharetra massa massa. Pulvinar etiam non quam lacus suspendisse 
    faucibus interdum. Ut tortor pretium viverra suspendisse potenti nullam ac tortor vitae. Sed felis eget velit aliquet 
    sagittis id. Sagittis id consectetur purus ut faucibus pulvinar elementum integer. Nunc mattis enim ut tellus. Sed 
    sed risus pretium quam. Tristique magna sit amet purus gravida quis blandit turpis cursus. Sit amet mauris commodo 
    quis imperdiet. Hendrerit gravida rutrum quisque non. Tortor condimentum lacinia quis vel eros donec ac odio tempor. 
    Nunc sed augue lacus viverra vitae congue. Erat velit scelerisque in dictum non consectetur a erat nam. Sit amet 
    tellus cras adipiscing enim.

    Nulla facilisi nullam vehicula ipsum a arcu cursus vitae congue. Ornare quam viverra orci sagittis eu volutpat odio 
    facilisis. Sapien eget mi proin sed libero enim sed faucibus. Amet nisl purus in mollis. Pretium nibh ipsum consequat 
    nisl vel pretium lectus quam id. In fermentum posuere urna nec tincidunt praesent semper feugiat. Pretium fusce id 
    velit ut tortor. Pharetra diam sit amet nisl suscipit. Elit scelerisque mauris pellentesque pulvinar. Quisque 
    sagittis purus sit amet. Dictum at tempor commodo ullamcorper a lacus. Sed odio morbi quis commodo odio aenean. Risus 
    nec feugiat in fermentum posuere urna. Gravida arcu ac tortor dignissim. In egestas erat imperdiet sed euismod nisi 
    porta lorem mollis. In fermentum posuere urna nec tincidunt praesent semper feugiat. Consequat semper viverra nam 
    libero justo laoreet sit amet.

    Lectus quam id leo in vitae turpis massa. Pellentesque nec nam aliquam sem. Nunc mi ipsum faucibus vitae aliquet nec 
    ullamcorper sit. At auctor urna nunc id cursus. Semper risus in hendrerit gravida. Cras sed felis eget velit aliquet 
    sagittis id consectetur purus. Senectus et netus et malesuada fames. At tempor commodo ullamcorper a lacus vestibulum 
    sed arcu. Rutrum tellus pellentesque eu tincidunt tortor aliquam. Habitasse platea dictumst quisque sagittis purus 
    sit amet. Odio eu feugiat pretium nibh ipsum consequat nisl vel pretium. Odio pellentesque diam volutpat commodo sed 
    egestas. Sed lectus vestibulum mattis ullamcorper. Non enim praesent elementum facilisis leo vel. Pellentesque eu 
    tincidunt tortor aliquam nulla facilisi cras. Nibh tortor id aliquet lectus proin nibh."""
    assert word_counter(text) == [('sed', 24), ('sit', 17), ('amet', 15), ('id', 13), ('in', 13), ('nunc', 11),
                                  ('eu', 11), ('arcu', 10), ('vitae', 10), ('odio', 10)]


def test_no_text():
    text = '.--. -.-- - .... --- -.'
    assert word_counter(text) == []


def test_none():
    text = None
    with pytest.raises(TypeError):
        word_counter(text)


if __name__ == '__main__':
    pytest.main()
