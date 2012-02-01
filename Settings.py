"""
Copyright (c) 2012 Timon Wong

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sublime

__all__ = ["get_settings", "get_setting_view", "get_setting"]

def get_settings():
    return sublime.load_settings("AStyleFormat.sublime-settings")

def get_setting_view(view, key, default = None):
    try:
        settings = view.settings()
        real_key = "AStyleFormat_%s" % key
        if settings.has(real_key):
            return settings.get(real_key)
    except:
        pass
    return get_settings().get(key, default)

def get_setting(key, default = None):
    return get_settings_view(sublime.active_window().active_view(), key, default)