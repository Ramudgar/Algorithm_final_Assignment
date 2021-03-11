def searching(self):
    print("Success")
    ent = self.search_entry.get()
    if ent != "":
        try:
            self.lis = []
            for i in self.emp_tree.get_children():
                a = self.emp_tree.item(i)['values'][0]
                self.lis.append(a)
            print(f"list = {self.lis}")
            search = self.linearsearch(self.lis, self.search_entry.get())
            print(f"search = {search}")
            if search:
                messagebox.showinfo("Success", "Found")
                query = "select * from employee where id = %s"
                values = (search,)
                a = self.db.select1(query, values)
                print(a)
                self.emp_tree.delete(*self.emp_tree.get_children())
                for i in a:
                    val = [i[0], i[4], i[2], i[6], i[5], i[7], i[8], i[9]]
                    self.emp_tree.insert('', END, values=val)

            else:
                messagebox.showerror("failed", "Error, Not found")

        except BaseException as m:
            print(m)
            messagebox.showerror("Not Found", "Error, Not found")


@classmethod
def linearsearch(self, lis, x):
    for i in range(len(lis)):
        if int(lis[i]) == int(x):
            return lis[i]
    return False


def sorting(self, events):
    if self.sort.get() == "By ID" and self.sort_t.get() == "Increasing":
        query = "select * from employee;"
        data = self.db.select(query)
        sort_val = []
        for values in data:
            sort_val.append(values)
        sorted_val = self.b_sort_a(sort_val)
        if len(sorted_val) != 0:
            messagebox.showinfo("Done", "Sorted increasing order")
            self.emp_tree.delete(*self.emp_tree.get_children())
            for i in sorted_val:
                val = [i[0], i[4], i[2], i[6], i[5], i[7], i[8], i[9]]
                self.emp_tree.insert('', END, values=val)

    elif self.sort.get() == "By ID" and self.sort_t.get() == "Decreasing":
        query = "select * from employee;"
        data = self.db.select(query)
        sort_val = []
        for values in data:
            sort_val.append(values)
        sorted_val = self.b_sort_d(sort_val)
        if len(sorted_val) != 0:
            messagebox.showinfo("Done", "Sorted Decreasing order")
            self.emp_tree.delete(*self.emp_tree.get_children())
            for i in sorted_val:
                val = [i[0], i[4], i[2], i[6], i[5], i[7], i[8], i[9]]
                self.emp_tree.insert('', END, values=val)


@classmethod
def b_sort_a(self, lis):
    for j in range(len(lis) - 1):
        for i in range(len(lis) - 1):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
    return lis


def b_sort_d(self, lis):
    for j in range(len(lis) - 1):
        for i in range(len(lis) - 1):
            if lis[i] < lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
    return lis
