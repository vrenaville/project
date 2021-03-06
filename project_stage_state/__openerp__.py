# -*- coding: utf-8 -*-
##############################################################################
#
#   Daniel Reis, 2014
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Add State field to Project Stages',
    'version': '1.0',
    'category': 'Project Management',
    'summary': 'Restore State attribute removed from Project Stages in 8.0',
    'author': 'Daniel Reis',
    'website': 'https://github.com/OCA/project-service',
    'depends': [
        'project',
    ],
    'data': [
        'project_view.xml',
        ],
    'installable': True,
}
