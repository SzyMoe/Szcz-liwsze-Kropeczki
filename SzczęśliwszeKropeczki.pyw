import tkinter as tk
from tkinter import messagebox as msb
import tkinter.scrolledtext as scrolledtext
import os
import random as r


try:
        os.mkdir('data')
        os.mkdir('data/files')
        os.mkdir('data/lottery files')
except:
        pass

start = 4
border = 0
for x in os.listdir("data/files"):
	border += 1
last = border % 4
error = False
change_variable = False
back = False
choosen_list = []
end = False
ButtonActivate = False
upsentList = []
choice = None

def rgb(rgb):
	return "#%02x%02x%02x" % rgb


def EditGroup(name, window):
	if name != "":
		if name + '.txt' in [x for x in os.listdir('data/files')]:
			msb.askokcancel("Uwaga!", "Aby program funkcjonował prawidłowo uczniowie muszą być zapisani według wzoru:"
									  "\n\n[Numer],[Imię] [Nazwisko]\n[Numer],[Imię] [Nazwisko]\n...\n\nNa przykład:"
									  "\n\n1,Adam Kowalski\n2,Ania Nowak\n[...]\n\nUwaga! Pomiędzy przecinkiem nie ma"
									  " spacji!")
			window.destroy()
			os.startfile("data\\files\\" + str(name) + '.txt')
			DataPage(root).GroupsText.config(state = 'normal')
		else:
			msb.showwarning("Błąd!", "Tej klasy nie ma w bazie danych! Spróbuj ponownie.")


def DeleteGroup(name, window):
	global change_variable
	if name != "":
		if str(name) + '.txt' in os.listdir('data/files'):
			MsgBox = msb.askokcancel("Uwaga", "Jesteś pewny, że chcesz usunąć klasę " + "''" + str(name) + "''?" )
			if MsgBox == True:
				window.destroy()
				change_variable = True

				os.remove("data\\files\\" + str(name) + '.txt')

				for x in os.listdir('data/files'):
					DataPage(root).GroupsText.insert(tk.END, "-->  " + x[:-4] + "\n")

				os.remove('data\\lottery files\\lottery_' + str(name) + '.txt')

				DataPage(root).GroupsText.config(state = 'normal')
				DataPage(root).GroupsText.delete('1.0', 'END')
		else:
			msb.showwarning("Błąd!", "Tej klasy nie ma w bazie danych! Spróbuj ponownie.")


def AddGroup(name, window):
	global change_variable
	if name != "":
		if name + '.txt' not in [x for x in os.listdir('data/files')]:
			MsgBox = msb.askokcancel("Uwaga!", "Aby program funkcjonował prawidłowo uczniowie muszą być zapisani "
											   "według wzoru:\n\n[Numer],[Imię] [Nazwisko]\n[Numer],[Imię] "
											   "[Nazwisko]\n[...]\n\nNa przykład:\n\n1,Adam Kowalski\n2,Ania "
											   "Nowak\n[...]\n\nUwaga! Pomiędzy przecinkiem nie ma spacji!")
			if MsgBox == True:
				window.destroy()
				change_variable = True
				try:
					f = open("data\\files\\"+ str(name) + '.txt', 'w+',  encoding='utf-8')
					os.startfile("data\\files\\" + str(name) + '.txt')

					for x in os.listdir('data/files'):
						DataPage(root).GroupsText.insert(tk.END, x[:-4] + '\n')

					DataPage(root).GroupsText.config(state = 'normal')
				except:
					pass
		else:
			msb.showwarning("Błąd!", "Klasa o takiej nazwie już istnieje.")


def EditGroupWindow():
	global ButtonActivate
	window = tk.Tk()
	window.title("Okienko do edytowania klas!")
	window.geometry('300x200')
	window.resizable(False, False)

	def EnableFucntion():
		window.destroy()

	window.protocol( "WM_DELETE_WINDOW", EnableFucntion)

	label = tk.Label(window, text = "Podaj nazwę klasy,\n którą chcesz edytować:", font = ('Courier', 14))
	label.place(relx = 0.1, rely = 0.05, relheight = 0.2, relwidth = 0.8)

	entry = tk.Entry(window, font = font)
	entry.place(relx = 0.1, rely = 0.3, relheight = 0.2, relwidth = 0.8)

	button = tk.Button(window, text = "Edytuj klasę", font = font, command = lambda: EditGroup(entry.get(), window))
	button.place(relx = 0.1, rely = 0.6, relheight = 0.2, relwidth = 0.8)

	window.attributes("-topmost", True)

	window.mainloop()


def DeleteGroupWindow():
	window = tk.Tk()
	window.title("Okienko do usuwania klas!")
	window.geometry('300x200')
	window.resizable(False, False)

	def EnableFucntion():
		window.destroy()

	window.protocol("WM_DELETE_WINDOW", EnableFucntion)

	label = tk.Label(window, text = "Podaj nazwę klasy,\n którą chcesz usunąć:", font = ('Courier', 14))
	label.place(relx = 0.1, rely = 0.05, relheight = 0.2, relwidth = 0.8)

	entry = tk.Entry(window, font = font)
	entry.place(relx = 0.1, rely = 0.3, relheight = 0.2, relwidth = 0.8)

	button = tk.Button(window, text = "Usuń klasę", font = font, command = lambda: DeleteGroup(entry.get(), window))
	button.place(relx = 0.1, rely = 0.6, relheight = 0.2, relwidth = 0.8)

	window.attributes("-topmost", True)

	window.mainloop()


def AddGroupWindow():
	window = tk.Tk()
	window.title("Okienko do dodawania klas!")
	window.geometry('300x200')
	window.resizable(False, False)

	def EnableFucntion():
		window.destroy()

	window.protocol( "WM_DELETE_WINDOW", EnableFucntion)

	label = tk.Label(window, text = "Podaj nazwę klasy,\n którą chcesz dodać:", font = ('Courier', 14))
	label.place(relx = 0.1, rely = 0.05, relheight = 0.2, relwidth = 0.8)

	entry = tk.Entry(window, font = font)
	entry.place(relx = 0.1, rely = 0.3, relheight = 0.2, relwidth = 0.8)

	button = tk.Button(window, text = "Dodaj klasę", font = font, command = lambda: AddGroup(entry.get(), window))
	button.place(relx = 0.1, rely = 0.6, relheight = 0.2, relwidth = 0.8)

	window.attributes("-topmost", True)

	window.mainloop()


def NewWindow(new_window, frame):
	global start
	global error
	global back

	if back is False:
		start = 4
		error = False
		frame.destroy()
		window = new_window(root)
	else:
		msb.showwarning("Uwaga!", "Zamknij okno losowania przed powrotem do menu.")


def Lottery(chancelabel, students, lenght, button, name, label, StudentCancel, UpsentButton):
	global choosen_list
	global choice
	global end
	global upsentList

	UpsentButton['state'] = 'normal'
	StudentCancel['state'] = 'normal'

	for student in upsentList:
		if student not in choosen_list:
			choosen_list.append(student)

	while True:
		if len(choosen_list) != lenght:
			choice = r.choice(students)
			end = False
			if choice not in choosen_list:
				break
			else:
				pass
		else:
			button['state'] = 'disabled'
			end = True
			label['text'] = 'Kliknij aby losować!'
			button['text'] = 'Nowa kolejka!'
			msb.showinfo("To już jest koniec... nie ma już nic!", "Koniec kolejki!")
			choice = None
			choosen_list = []
			open('data\\lottery files\\lottery_' + name, 'w',  encoding='utf-8').close()
			button['state'] = 'normal'
			chancelabel['text'] = 'Szansa na wylosowanie ucznia: X%'
			break

	if end is False:
		button['text'] = 'Losuj'
		try:
			var = str(choice).split(' ')
			label['text'] =	var[0] + '\n' + var[1] + '\n' + var[2]
			choosen_list.append(choice)
		except:
			pass
		try:
			chancelabel['text'] = 'Szansa na wylosowanie ucznia: ' + str(int(round(1/(len(open('data\\files\\' + name).readlines()) - len(choosen_list)), 2)*100)) + '%'
		except:
			chancelabel['text'] = 'Szansa na wylosowanie ucznia: ...%'
	else:
		pass


def upsent(UpsentButton):
	global choice
	global upsentList

	if choice is not None:
		if choice not in upsentList:
			upsentList.append(choice)

		msb.showinfo('Uczeń nieobecny!', 'Wylosowany uczeń został usunięty z kolejki '
										 'do momentu ponownego uruchomienia okna losowania.')
		UpsentButton['state'] = 'disabled'
	else:
		msb.showerror('Błąd!', 'Brak ucznia!')


def StudentCancelButton(StudentCancel):
	global choice
	global choosen_list
	if choice is not None:
		choosen_list.remove(choice)
		msb.showinfo('Cofnięto ucznia!', "Wylosowany uczeń został cofnięty i włożony spowrotem do kolejki.")
		StudentCancel['state'] = 'disabled'
	else:
		msb.showerror('Błąd', 'Brak ucznia')


def LotteryWindow(name, d):
	global choosen_list
	global back
	students = []
	lenght = 0

	for x in open('data\\files\\' + name, 'r', encoding="utf-8"):
		students.append(x.strip().replace(',', ' '))
		lenght += 1

	back = True
	try:
		for x in open('data\\lottery files\\lottery_' + name, 'r', encoding='utf-8'):
			choosen_list.append(''.join(x.strip().split(',')))
	except:
		f = open('data\\lottery files\\lottery_' + name, 'w+',encoding='utf-8')

	def Exit():
		global choosen_list
		global back
		global upsentList

		upsentList = []

		open('data\\lottery files\\lottery_' + name, 'w').close()
		f = open('data\\lottery files\\lottery_' + name, 'a',  encoding='utf-8')
		txt = ''

		for x in choosen_list:
			for y in x:
				txt += y
			txt += '\n'
		f.write(txt)
		choosen_list = []
		back = False
		try:
			for x in d:
				d[x].config(state = 'normal')
		except:
			pass
		window.destroy()

	window = tk.Tk()
	window.geometry('500x400')
	window.attributes("-topmost", True)
	window.protocol( "WM_DELETE_WINDOW", Exit)
	window.title(name[:-4])
	window.resizable(False, False)
	window.title('Losowanko!')

	for x in d:
		d[x].config(state = 'disabled')

	frame = tk.Frame(window, bg = 'grey')
	frame.place(relwidth = 1, relheight = 1)

	ChanceLabel = tk.Label(window, text = "Szansa na wylosowanie ucznia: X%", font = ('Courier', 16), bg = 'grey', anchor = 'w', fg = 'white')
	ChanceLabel.place(relx = 0.05, rely = 0.9, relwidth = 1, relheight = 0.1)

	try:
		ChanceLabel['text'] = 'Szansa na wylosowanie ucznia: ' + str(int(round(1/(len(open('data\\files\\' + name).readlines()) - len(choosen_list)), 2)*100)) + '%'
	except:
		ChanceLabel['text'] = 'Szansa na wylosowanie ucznia: X%'

	DisplayLabel = tk.Label(window, text = "Kilknij aby losować!", font = ('Courier', 25), fg = 'white', bg = 'grey', anchor = 'center')
	DisplayLabel.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.4)

	StudentCancel = tk.Button(frame, text = 'Cofnij', font = ('Courier', 15), command = lambda: StudentCancelButton(StudentCancel))
	StudentCancel.place(relx = 0.15, rely = 0.75, relwidth = 0.3, relheight = 0.15)

	Upsent = tk.Button(frame, text = "Nieobecny", font = ('Courier', 15), command = lambda: upsent(Upsent))
	Upsent.place(relx = 0.55, rely = 0.75, relwidth = 0.3, relheight = 0.15)

	ActionButton = tk.Button(frame, text = "Losuj", font = font, command = lambda: Lottery(ChanceLabel, students, lenght, ActionButton, name, DisplayLabel, StudentCancel, Upsent))
	ActionButton.place(relx = 0.15, rely = 0.50, relwidth = 0.7, relheight = 0.2)

	window.mainloop()


class StartPage:
	def __init__(self, master):

		frame = tk.Frame(master, bg = 'grey')
		frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

		self.LotteryButton = tk.Button(frame, text = 'Losowanie', font = font, command = lambda: NewWindow(LotteryPage, frame))
		self.LotteryButton.place(relx = 0.25, rely = 0.25, relwidth = 0.5, relheight = 0.15)

		self.EditButton = tk.Button(frame, text = "Baza danych", font = font, command = lambda: NewWindow(DataPage, frame))
		self.EditButton.place(relx = 0.25, rely = 0.45, relwidth = 0.5, relheight = 0.15)

		self.QuitButton = tk.Button(frame, text = 'Wyjdź', font = font, command = lambda: root.destroy())
		self.QuitButton.place(relx = 0.25, rely = 0.65, relwidth = 0.5, relheight = 0.15)

		self.MyOwnLabel = tk.Label(frame, text = "Szymon Molęda\n2020", font = ('Courier', 15), bg = 'grey', foreground = 'white')
		self.MyOwnLabel.place(relx = 0.35, rely = 0.88, relwidth = 0.3, relheight = 0.1)

		self.TitleLabel = tk.Label(frame, text = 'Szczęśliwsze\nKropeczki', font = ('Courier', 30), bg = 'grey', foreground = 'white')
		self.TitleLabel.place(relx = 0.25, rely = 0.05, relwidth = 0.5, relheight = 0.15)


class LotteryPage:
	global change_variable

	def __init__(self, master):
		global start

		if change_variable is False:

			frame = tk.Frame(master, bg = 'grey')
			frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

			self.LotteryFrame = tk.Label(frame, bg = 'grey')
			self.LotteryFrame.place(relx = 0.1, rely = 0.15, relwidth = 0.8, relheight = 0.7)

			d = {}
			for name in enumerate(os.listdir('data/files')):
				d['button{}'.format(name[0])] = tk.Button(self.LotteryFrame, text = str(name[1][:-4]), height = 3, width = 30, font = ('Courier', 16), command = lambda name = name[1]: LotteryWindow(name, d))

			try:
				for x in range(start):
					d['button{}'.format(x)].pack(pady = 6)
			except:
				pass

			self.label = tk.Label(frame, text = 'Wybierz klasę', font = ('Courier', 30), bg = 'grey', fg = 'white')
			self.label.place(relx = 0.14, rely = 0.03, relwidth = 0.72, relheight = 0.1)

			self.NextButton = tk.Button(frame, text = "---->", font = ('Courier', 16), command = lambda: NextPage(d, self.NextButton))
			self.NextButton.place(rely = 0.875, relx = 0.7, relwidth = 0.2, relheight = 0.1)

			self.PreviousButton = tk.Button(frame, text = "<----", font = ('Courier', 16), command = lambda: PreviousPage(d, self.NextButton))
			self.PreviousButton.place(rely = 0.875, relx = 0.1, relwidth = 0.2, relheight = 0.1)

			if len(d) <= 4:
				self.NextButton.config(state = 'disabled')
				self.PreviousButton.config(state = 'disabled')

			self.BackButton = tk.Button(frame, text = "Powrót", command = lambda: NewWindow(StartPage, frame), font = font)
			self.BackButton.place(rely = 0.875, relx = 0.35,relwidth = 0.3, relheight = 0.1)

		else:
			global window
			window = StartPage(root)
			msb.showwarning("Uwaga!", "Dokonałeś zmian w bazie danych, konieczne jest ponowne uruchomienie aplikacji.")

		def NextPage(d, button):
			global start
			global error
			global last
			global border

			try:
				for x in range(start):
					d['button{}'.format(x)].pack_forget()
				for x in range(start, start + 4):
					d['button{}'.format(x)].pack(pady = 6)
				if border % 4 == 0:
					button['state'] = 'disabled'
			except:
				error = True
				start = start - 4
			start = start + 4

		def PreviousPage(d, button):
			global start
			global last
			global error
			button['state'] = 'normal'
			if start >= 4:
				if error == False:
					for x in range(start):
						d['button{}'.format(x)].pack_forget()
					try:
						for x in range(start - 8, start - 4):
							d['button{}'.format(x)].pack(pady = 6)
					except:
						for x in range(start):
							d['button{}'.format(x)].pack(pady = 6)
						start += 4
				else:
					for x in range(border - 1, border - last - 1, -1):
						d['button{}'.format(x)].pack_forget()
					for x in range(start - 4, start):
						d['button{}'.format(x)].pack(pady = 6)
					start = start + 4
					error = False
				start = start - 4


class DataPage:
	def __init__(self, master):

		frame = tk.Frame(master, bg = 'grey')
		frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

		self.GroupsText = scrolledtext.ScrolledText(frame, bg = 'white', font = ('Courier', 16))
		self.GroupsText.place(relx = 0.3, rely = 0.05, relwidth = 0.6, relheight = 0.8)

		self.AddGroupButton = tk.Button(frame, text = "Dodaj Klasę", font = ('Courier', 10), command = lambda: AddGroupWindow())
		self.AddGroupButton.place(relx = 0.05, rely = 0.05, relwidth = 0.2, relheight = 0.1)

		self.DeleteButton = tk.Button(frame, text = "Usuń Klasę", font = ('Courier', 10), command = lambda:	DeleteGroupWindow())
		self.DeleteButton.place(relx = 0.05, rely = 0.3, relwidth = 0.2, relheight = 0.1)

		self.GroupsText.insert(tk.END, 'Klasy w bazie danych:\n\n', ('p'))
		self.GroupsText.tag_add('p', '1.0', '1.0')
		self.GroupsText.tag_config('p', font = ('Courier', 18))

		for x in os.listdir('data/files'):
			self.GroupsText.insert(tk.END, "-->  " + x[:-4] + "\n")

		self.GroupsText.config(state="disabled")

		self.EditGroupButton = tk.Button(frame, text = 'Edytuj klasę', font = ('Courier', 10), command = lambda: EditGroupWindow())
		self.EditGroupButton.place(relx = 0.05, rely = 0.55, relwidth = 0.2, relheight = 0.1)

		self.BackButton = tk.Button(frame, text = "Powrót", font = font, command = lambda: NewWindow(StartPage, frame))
		self.BackButton.place(rely = 0.875, relx = 0.1, relwidth = 0.8, relheight = 0.1)


root = tk.Tk()
root.geometry('800x800')
root.title('Szczęśliwsze kropeczki')
font = ('Courier', 20)
root.iconbitmap('icon.ico')
root.resizable(False, False)

background_image = tk.PhotoImage(file ='bg.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relheight = 1, relwidth = 1)

window = StartPage(root)
root.mainloop()
