# -*- coding:Utf-8 -*-
###############################################################################
## Lutris
##
## Copyright (C) 2009 Mathieu Comandon strycore@gmail.com
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
###############################################################################

"""Container for game config options"""

from gi.repository import Gtk

from lutris.runners import import_runner
from lutris.gui.configvbox import ConfigVBox


class GameConfigVBox(ConfigVBox):
    """VBox for game options"""
    def __init__(self, lutris_config, caller):
        ConfigVBox.__init__(self, "game", caller)
        self.lutris_config = lutris_config
        self.lutris_config.config_type = "game"
        self.runner_class = self.lutris_config.runner
        runner = import_runner(self.runner_class)()

        if runner.game_options:
            self.options = runner.game_options
            self.generate_widgets()
        else:
            no_option_label = Gtk.Label(label="No game options")
            self.pack_start(no_option_label, True, True, 0)
