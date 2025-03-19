class node:
    def __init__(self,name):
        self.info=name
        self.link=None

class LinkedList:
    def __init__(self):
        self.start=None

    def Insertion_atThe_End(self,item):
        nd = node(item)
        if self.start == None:
            self.start=nd
            return
        temp =self.start
        while temp.link != None:
            temp = temp.link
        temp.link=nd

    def Insertion_atThe_Beg(self,item):
        nd = node(item)
        nd.link = self.start
        self.start=nd

    def Insertion_After_SpecificItem(self,item,value):
        temp=self.start
        while temp !=None:
            if temp.info == item:
                nd=node(value)
                nd.link=temp.link
                temp.link=nd
                return
            temp=temp.link
        print(f"item'{item}'not found in the list.")


    def display(self):
        temp=self.start
        while temp != None:
            print(temp.info, end=" > ")
            temp=temp.link
        print("None")


ob = LinkedList()
ob.Insertion_atThe_End("taniya")
ob.Insertion_atThe_Beg("arpita")
ob.Insertion_After_SpecificItem("taniya","arpita")
ob.display()




