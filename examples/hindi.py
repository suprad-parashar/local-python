# आसान गणित

अ = पूर्णांक(पढ़ो("पहला संख्या: "))
कार्य = पढ़ो("क्या करना चाहेंगे?: ")
ब = पूर्णांक(पढ़ो("दूसरा संख्या: "))
सही = सच

मिलान कार्य:
	विकल्प "+":
		ई = अ + ब
	विकल्प "-":
		ई = अ - ब
	विकल्प "*":
		ई = अ * ब
	विकल्प "/":
		ई = अ / ब
	विकल्प "%":
		ई = अ % ब
	विकल्प _:
		लिखो("कोई विकल्प नहीं है!")
		सही = झूट

अगर सही:
	लिखो("दोनों संख्यों का मिलन: " + अक्षर(ई))