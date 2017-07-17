class Fun():
	def Accp(self):
		str=raw_input("input a string: ")
		self.str=str

	def Printstr(self):
		print "string is: ",self.str

st=Fun()
st.Accp()
st.Printstr()