

import sqlite3
import sys


def letsgo1(conn):
	c0 = conn.cursor()
	c1 = conn.cursor()
	c0.execute("SELECT FULL, FAVOR, ADDON, NAME, POT, MATERIALS from foods where GOOD = \"{}\"".format(sys.argv[2]))
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
def letsgo2(conn):
	c0 = conn.cursor()
	c0.execute("SELECT LOCATION, ADDRESS, THING from collection_infos where QUALITY = \"{}\" ORDER BY THING".format(sys.argv[2]))
	thing = None
	for row in c0:
		if thing != row[2]:
			thing = row[2]
			print(thing)
		print("\t" + row[0] + " "+ row[1])

def letsgo3(conn):
	c0 = conn.cursor()
	c0.execute("SELECT LOCATION, ADDRESS from collection_infos where THING = \"{}\"".format(sys.argv[2]))
	for row in c0:
		print(row[0] + " " + row[1])


import os
def main():
	the_path = os.path.dirname(sys.argv[0])
	os.chdir(the_path)
	if(len(sys.argv)!= 3):
		print("example:\n\tpython ...py 人物 渡会 ---- 得到该人物绝赞的菜")
		print("\tpython ...py 品质 紫色 ---- 得到所有紫色物品的采集地点")
		print("\tpython ...py 物品 佛珠 ---- 得到佛珠的采集地点")
		return
	conn = sqlite3.connect("collections.db")
	if sys.argv[1] == "人物":
		letsgo1(conn)
	elif sys.argv[1] == "品质":
		letsgo2(conn)
	elif sys.argv[1] == "物品":
		letsgo3(conn)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()