

import sqlite3
import sys


def letsgo3():
	conn = sqlite3.connect("collections.db")
	c0 = conn.cursor()
	c1 = conn.cursor()
	c0.execute("SELECT FULL, FAVOR, ADDON, NAME, POT, MATERIALS from foods where GOOD = \"{}\"".format(sys.argv[1]))
	for row in c0:
		print("菜名  ：" + row[3])
		print("饱食度：" + str(row[0]))
		print("好感度：" + str(row[1]))
		print("锅具  ：" + str(row[4]))
		material = row[5].split(":")
		for mat in material:
			c1.execute("SELECT LOCATION, ADDRESS from collection_infos where THING = \"{}\"".format(mat))
			print("\t", mat)
			for row2 in c1:
				print("\t\t", row2[0], row2[1])
	conn.commit()
	conn.close()
def main():
	if(len(sys.argv)!= 2):
		print("example:\npython ...py 渡会")
	letsgo3()


if __name__ == '__main__':
	main()