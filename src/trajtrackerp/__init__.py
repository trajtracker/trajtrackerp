"""

TrajTracker - paradigms package

@author: Dror Dotan
@copyright: Copyright (c) 2017, Dror Dotan

This file is part of TrajTracker.

TrajTracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

TrajTracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with TrajTracker.  If not, see <http://www.gnu.org/licenses/>.
"""

def version():
    """
    Returns the package version as a tuple with 3 items: #major, #minor, #bugfix
    """
    return 1, 2, 0


def version_str():
    """ Returns the package version as a string: major.minor.bugfix """
    v = version()
    return '{:}.{:}.{:}'.format(v[0], v[1], v[2])


from ._res import resources_dir, sounds_dir, images_dir

import trajtrackerp.common
import trajtrackerp.num2pos
