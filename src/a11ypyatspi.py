################################################################################
##                                                                            ##
## This file is a part of TADEK.                                              ##
##                                                                            ##
## TADEK - Test Automation in a Distributed Environment                       ##
## (http://tadek.comarch.com)                                                 ##
##                                                                            ##
## Copyright (C) 2011 Comarch S.A.                                            ##
## All rights reserved.                                                       ##
##                                                                            ##
## TADEK is free software for non-commercial purposes. For commercial ones    ##
## we offer a commercial license. Please check http://tadek.comarch.com for   ##
## details or write to tadek-licenses@comarch.com                             ##
##                                                                            ##
## You can redistribute it and/or modify it under the terms of the            ##
## GNU General Public License as published by the Free Software Foundation,   ##
## either version 3 of the License, or (at your option) any later version.    ##
##                                                                            ##
## TADEK is distributed in the hope that it will be useful,                   ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of             ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              ##
## GNU General Public License for more details.                               ##
##                                                                            ##
## You should have received a copy of the GNU General Public License          ##
## along with TADEK bundled with this file in the file LICENSE.               ##
## If not, see http://www.gnu.org/licenses/.                                  ##
##                                                                            ##
## Please notice that Contributor Agreement applies to any contribution       ##
## you make to TADEK. The Agreement must be completed, signed and sent        ##
## to Comarch before any contribution is made. You should have received       ##
## a copy of Contribution Agreement along with TADEK bundled with this file   ##
## in the file CONTRIBUTION_AGREEMENT.pdf or see http://tadek.comarch.com     ##
## or write to tadek-licenses@comarch.com                                     ##
##                                                                            ##
################################################################################

import pyatspi

from interface import *
from constants import *

_DESKTOP = 0

#
# Implement accessibility constants:
#
actionset = ActionSet()
actionset.ACTIVATE = "activate"
actionset.CLICK = "click"
actionset.CONTRACT = "expand and contract"
actionset.EDIT = "edit"
actionset.EXPAND = "expand and contract"
actionset.PRESS = "press"
actionset.RELEASE = "release"

buttonset = ButtonSet()
(
    buttonset.LEFT,
    buttonset.MIDDLE,
    buttonset.RIGHT
) = range(3)

relationset = RelationSet()
relationset.CHILD_CELL_OF = pyatspi.RELATION_NODE_CHILD_OF
relationset.LABEL_FOR = pyatspi.RELATION_LABEL_FOR
relationset.LABELED_BY = pyatspi.RELATION_LABELLED_BY

roleset = RoleSet()
roleset.ACCELERATOR_LABEL = pyatspi.ROLE_ACCELERATOR_LABEL
roleset.ALERT = pyatspi.ROLE_ALERT
roleset.APPLICATION = pyatspi.ROLE_APPLICATION
roleset.BUTTON = pyatspi.ROLE_PUSH_BUTTON
roleset.CANVAS = pyatspi.ROLE_CANVAS
roleset.CHECK_BOX = pyatspi.ROLE_CHECK_BOX
roleset.CHECK_MENU_ITEM = pyatspi.ROLE_CHECK_MENU_ITEM
roleset.COMBO_BOX = pyatspi.ROLE_COMBO_BOX
roleset.DIALOG = pyatspi.ROLE_DIALOG
roleset.DRAWING_AREA = pyatspi.ROLE_DRAWING_AREA
roleset.EDITBAR = pyatspi.ROLE_EDITBAR
roleset.ENTRY = pyatspi.ROLE_ENTRY
roleset.FILE_CHOOSER = pyatspi.ROLE_FILE_CHOOSER
roleset.FILLER = pyatspi.ROLE_FILLER
roleset.FRAME = pyatspi.ROLE_FRAME
roleset.ICON = pyatspi.ROLE_ICON
roleset.IMAGE = pyatspi.ROLE_IMAGE
roleset.LABEL = pyatspi.ROLE_LABEL
roleset.LINK = pyatspi.ROLE_LINK
roleset.LIST = pyatspi.ROLE_LIST
roleset.LIST_ITEM = pyatspi.ROLE_LIST_ITEM
roleset.MENU = pyatspi.ROLE_MENU
roleset.MENU_BAR = pyatspi.ROLE_MENU_BAR
roleset.MENU_ITEM = pyatspi.ROLE_MENU_ITEM
roleset.PAGE = pyatspi.ROLE_PAGE
roleset.PAGE_TAB = pyatspi.ROLE_PAGE_TAB
roleset.PAGE_TAB_LIST = pyatspi.ROLE_PAGE_TAB_LIST
roleset.PANEL = pyatspi.ROLE_PANEL
roleset.PASSWORD_TEXT = pyatspi.ROLE_PASSWORD_TEXT
roleset.POPUP_MENU = pyatspi.ROLE_POPUP_MENU
roleset.PROGRESS_BAR = pyatspi.ROLE_PROGRESS_BAR
roleset.RADIO_BUTTON = pyatspi.ROLE_RADIO_BUTTON
roleset.RADIO_MENU_ITEM = pyatspi.ROLE_RADIO_MENU_ITEM
roleset.SCROLL_BAR = pyatspi.ROLE_SCROLL_BAR
roleset.SCROLL_PANE = pyatspi.ROLE_SCROLL_PANE
roleset.SEPARATOR = pyatspi.ROLE_SEPARATOR
roleset.SLIDER = pyatspi.ROLE_SLIDER
roleset.SPIN_BUTTON = pyatspi.ROLE_SPIN_BUTTON
roleset.SPLIT_PANE = pyatspi.ROLE_SPLIT_PANE
roleset.STATUS_BAR = pyatspi.ROLE_STATUS_BAR
roleset.TABLE = pyatspi.ROLE_TABLE
roleset.TABLE_CELL = pyatspi.ROLE_TABLE_CELL
roleset.TABLE_COLUMN_HEADER = pyatspi.ROLE_TABLE_COLUMN_HEADER
roleset.TABLE_ROW_HEADER = pyatspi.ROLE_TABLE_ROW_HEADER
roleset.TEXT = pyatspi.ROLE_TEXT
roleset.TOGGLE_BUTTON = pyatspi.ROLE_TOGGLE_BUTTON
roleset.TOOL_BAR = pyatspi.ROLE_TOOL_BAR
roleset.TREE = pyatspi.ROLE_TREE
roleset.TREE_TABLE = pyatspi.ROLE_TREE_TABLE
roleset.UNKNOWN = pyatspi.ROLE_UNKNOWN
roleset.VIEWPORT = pyatspi.ROLE_VIEWPORT
roleset.WINDOW = pyatspi.ROLE_WINDOW

stateset = StateSet()
stateset.ACTIVE = pyatspi.STATE_ACTIVE
stateset.CHECKED = pyatspi.STATE_CHECKED
stateset.COLLAPSED = pyatspi.STATE_COLLAPSED
stateset.EDITABLE = pyatspi.STATE_EDITABLE
stateset.ENABLED = pyatspi.STATE_ENABLED
stateset.EXPANDABLE = pyatspi.STATE_EXPANDABLE
stateset.EXPANDED = pyatspi.STATE_EXPANDED
stateset.FOCUSABLE = pyatspi.STATE_FOCUSABLE
stateset.FOCUSED = pyatspi.STATE_FOCUSED
stateset.MULTILINE = pyatspi.STATE_MULTI_LINE
stateset.MULTISELECTABLE = pyatspi.STATE_MULTISELECTABLE
stateset.SELECTABLE = pyatspi.STATE_SELECTABLE
stateset.SELECTED = pyatspi.STATE_SELECTED
stateset.SENSITIVE = pyatspi.STATE_SENSITIVE
stateset.SHOWING = pyatspi.STATE_SHOWING
stateset.VISIBLE = pyatspi.STATE_VISIBLE

#
# Implement accessibility interface:
#
class PyAtSpi(IAccessibility):
    '''
    An implementation of accessibility interface for Python AT-SPI
    (pyatspi) library.
    '''
    name = "AT-SPI"
    actionset = actionset
    buttonset = buttonset
    keyset = keyset
    relationset = relationset
    roleset = roleset
    stateset = stateset

# Device:
    def mouseClick(self, x, y, button):
        if button == buttonset.LEFT:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B1C)
        elif button == buttonset.MIDDLE:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B2C)
        elif button == buttonset.RIGHT:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B3C)
        else:
            raise AccessibilityError("Mouse 'click' event of button '%s' is not"
                                     " implemented" % button)

    def mouseDoubleClick(self, x, y, button):
        if button == buttonset.LEFT:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B1D)
        elif button == buttonset.MIDDLE:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B2D)
        elif button == buttonset.RIGHT:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B3D)
        else:
            raise AccessibilityError("Mouse 'double-click' event of button '%s'"
                                     " is not implemented" % button)

    def mousePress(self, x, y, button):
        if button == buttonset.LEFT:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B1P)
        elif button == buttonset.MIDDLE:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B2P)
        elif button == buttonset.RIGHT:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B3P)
        else:
            raise AccessibilityError("Mouse 'press' event of button '%s' is not"
                                     " implemented" % button)

    def mouseRelease(self, x, y, button):
        if button == buttonset.LEFT:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B1R)
        elif button == buttonset.MIDDLE:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B2R)
        elif button == buttonset.RIGHT:
            pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_B3R)
        else:
            raise AccessibilityError("Mouse 'release' event of button '%s' is"
                                     " not implemented" % button)

    def mouseAbsoluteMotion(self, x, y):
        pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_ABS)

    def mouseRelativeMotion(self, x, y):
        pyatspi.Registry.generateMouseEvent(x, y, pyatspi.MOUSE_REL)

    def _keyboardEvent(self, keycode, modifiers):
        for modifier in modifiers:
            pyatspi.Registry.generateKeyboardEvent(modifier, None,
                                                   pyatspi.KEY_PRESS)
        pyatspi.Registry.generateKeyboardEvent(keycode, None, pyatspi.KEY_SYM)
        for modifier in modifiers:
            pyatspi.Registry.generateKeyboardEvent(modifier, None,
                                                   pyatspi.KEY_RELEASE)

# Object children:
    def getDesktop(self):
        return pyatspi.Registry.getDesktop(_DESKTOP)

    def children(self, parent=None):
        if parent is None:
            parent = self.getDesktop()
        try:
            for child in parent:
                yield child
        except Exception:
            pass

    def countChildren(self, parent=None):
        if parent is None:
            parent = self.getDesktop()
        try:
            return parent.childCount
        except Exception:
            return 0

    def _getChild(self, parent, index):
        if parent is None:
            parent = self.getDesktop()
        try:
            return parent.getChildAtIndex(index)
        except Exception:
            return None

    def getParent(self, accessible):
        try:
            return accessible.parent
        except Exception:
            return None

# Object properties:
    def getIndex(self, accessible):
        try:
            index = accessible.getIndexInParent()
            if (index == -1 and
                isinstance(accessible, pyatspi.Accessibility.Application)):
                for i, app in enumerate(self.children()):
                    if accessible == app:
                        index = i
                        break
            return index
        except Exception:
            return -1

    @decodeResult()
    def getName(self, accessible):
        try:
            return accessible.name
        except Exception:
            return None

    @decodeResult()
    def getDescription(self, accessible):
        try:
            return accessible.description
        except Exception:
            return None

    def getRole(self, accessible):
        try:
            return accessible.getRole()
        except Exception:
            return None

    def getPosition(self, accessible):
        try:
            component = accessible.queryComponent()
            return component.getPosition(pyatspi.DESKTOP_COORDS)
        except Exception:
            return None

    def getSize(self, accessible):
        try:
            return accessible.queryComponent().getSize()
        except Exception:
            return None

    def getAttributes(self, accessible):
        try:
            attrlist = accessible.getAttributes()
        except Exception:
            return None
        attrs = {}
        for attr in attrlist:
            name, value = attr.split(':', 1)
            attrs[name] = value
        return attrs

    @decodeResult()
    def getText(self, accessible):
        try:
            return accessible.queryText().getText(0, -1)
        except Exception:
            return None

    @encodeLastArg()
    def setText(self, accessible, text):
        try:
            return accessible.queryEditableText().setTextContents(text)
        except Exception:
            return False

    def getValue(self, accessible):
        try:
            value = accessible.queryValue()
            if value is None:
                return None
            return value.currentValue
        except Exception:
            return None

    def setValue(self, accessible, value):
        try:
            val = accessible.queryValue()
            if val is None:
                return False
            val.currentValue = value
            return True
        except Exception:
            return False

    def getImage(self, accessible):
        try:
            return accessible.queryImage()
        except Exception:
            return None

    def grabFocus(self, accessible):
        try:
            return accessible.queryComponent().grabFocus()
        except Exception:
            return False

# Object actions:
    def actions(self, accessible):
        try:
            action = accessible.queryAction()
            for i in xrange(action.nActions):
                yield action.getName(i)
        except Exception:
            pass

    def doAction(self, accessible, action):
        name = action
        try:
            action = accessible.queryAction()
            num = None
            for i in xrange(action.nActions):
                if action.getName(i) == name:
                    num = i
                    break
            if num is None:
                return False
            return action.doAction(num)
        except Exception:
            raise
            return False

# Object relations:
    def relations(self, accessible):
        try:
            for relation in accessible.getRelationSet():
                yield relation.getRelationType()
        except Exception:
            pass

    def relationTargets(self, accessible, relation):
        try:
            for rel in accessible.getRelationSet():
                if rel.getRelationType() == relation:
                    for i in xrange(rel.getNTargets()):
                        yield rel.getTarget(i)
                    break
        except Exception:
            pass

# Object states:
    def states(self, accessible):
        try:
            return iter(accessible.getState().getStates())
        except Exception:
            return iter(())

    def inState(self, accessible, state):
        try:
            return accessible.getState().contains(state)
        except Exception:
            return False

