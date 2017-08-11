import os.path

import pytest

import sunpy.tests

root_dir = os.path.dirname(os.path.abspath(sunpy.__file__))


def test_main_nonexisting_module():
    with pytest.raises(ImportError):
        sunpy.tests.main('doesnotexist')


def test_main_stdlib_module():
    """This test makes sure that the module is really searched within the
    sunpy package.

    """
    with pytest.raises(ImportError):
        sunpy.tests.main('random')


def test_main_noargs(monkeypatch):
    monkeypatch.setattr(pytest, 'main', lambda x: x)
    args = sunpy.tests.main()
    assert args in (['-k-online', '-m not figure', '-p no:warnings', 'sunpy'],
                    ['-k-online', '-m not figure', '-p no:warnings', root_dir])


def test_main_submodule(monkeypatch):
    monkeypatch.setattr(pytest, 'main', lambda x: x)
    args = sunpy.tests.main('map')
    assert args in (['-k-online', '-m not figure', '-p no:warnings'] + [os.path.join('sunpy', 'map')],
                    ['-k-online', '-m not figure', '-p no:warnings'] + [os.path.join(root_dir, 'map')])


def test_main_submodule(monkeypatch):
    monkeypatch.setattr(pytest, 'main', lambda x: x)
    args = sunpy.tests.main('net.jsoc')
    assert args in (['-k-online', '-m not figure', '-p no:warnings'] + [os.path.join('sunpy', 'net', 'jsoc')],
                    ['-k-online', '-m not figure', '-p no:warnings'] + [os.path.join(root_dir, 'net', 'jsoc')])


def test_main_with_cover(monkeypatch):
    monkeypatch.setattr(pytest, 'main', lambda x: x)
    args = sunpy.tests.main('map', coverage=True)
    covpath = os.path.abspath(
        os.path.join(sunpy.tests.testdir, os.path.join(os.pardir, 'map')))
    assert args in (['--cov', covpath, '-k-online', '-m not figure', '-p no:warnings', os.path.join('sunpy', 'map')],
                    ['--cov', os.path.join('sunpy', 'map'), '-k-online', '-m not figure', '-p no:warnings', os.path.join(root_dir, 'map')],
                    ['--cov', os.path.join('sunpy', 'map'), '-k-online', '-m not figure', '-p no:warnings', os.path.join('sunpy', 'map')],
                    ['--cov', covpath, '-k-online', '-m not figure', '-p no:warnings', os.path.join(root_dir, 'map')])


def test_main_with_show_uncovered_lines(monkeypatch):
    monkeypatch.setattr(pytest, 'main', lambda x: x)
    args = sunpy.tests.main('map', cov_report='term-missing')
    assert args in (['--cov-report', 'term-missing', '-k-online', '-m not figure',
                     '-p no:warnings', os.path.join('sunpy', 'map')],
                    ['--cov-report', 'term-missing', '-k-online', '-m not figure',
                     '-p no:warnings', os.path.join(root_dir, 'map')])


def test_main_exclude_online(monkeypatch):
    monkeypatch.setattr(pytest, 'main', lambda x: x)
    args = sunpy.tests.main('map', online=False)
    assert args in (['-k-online', '-m not figure', '-p no:warnings', os.path.join('sunpy', 'map')],
                    ['-k-online', '-m not figure', '-p no:warnings', os.path.join(root_dir, 'map')])


def test_main_only_online(monkeypatch):
    monkeypatch.setattr(pytest, 'main', lambda x: x)
    args = sunpy.tests.main('map', offline=False, online=True)
    assert args in (['-k online', '-m not figure', '-p no:warnings', os.path.join('sunpy', 'map')],
                    ['-k online', '-m not figure', '-p no:warnings', os.path.join(root_dir, 'map')])


def test_main_figures(monkeypatch):
    monkeypatch.setattr(pytest, 'main', lambda x: x)
    args = sunpy.tests.main(figure=True)
    assert args in (['-k-online', '-p no:warnings', 'sunpy'],
                    ['-k-online', '-p no:warnings', root_dir])

