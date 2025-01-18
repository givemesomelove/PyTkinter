import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import rootUI,labelUI, buttonUI, entryUI, textUI, frameUI, checkboxUI, radiobuttonUI
import listboxUI, spinboxUI, canvasUI, menuUI, packUI, gridUI, placeUI, panedWindowUI
import ttkUI, comboboxUI, notebookUI, progressbarUI, treeviewUI

def main():

    root = rootUI.makeRoot()
    print(tk.TkVersion)

    # labelUI.makeLabl(root)
    
    # buttonUI.makeButton(root)

    # entryUI.makeEntry(root)

    # textUI.makeText(root)

    # frameUI.makeFrame(root)

    # checkboxUI.makeCheckbox(root)

    # radiobuttonUI.makeRadiobutton(root)

    # listboxUI.makeListbox(root)

    # spinboxUI.makeSpinbox(root)

    # canvasUI.makeCanvasUI(root)

    # packUI.makePack(root)

    # gridUI.makeGrid(root)

    treeviewUI.makeTreeview(root)

    root.mainloop()

if __name__ == '__main__':
    main()
