import xlrd
import sqlite3







def formatList(cur_list):
	flag = False
	res = ""
	for cur_value in cur_list:
		if flag:
			res = res + ":"
		else:
			flag = True
		res = res + cur_value
	return res

def emptyDB(conn):
	c0 = conn.cursor()
	c0.execute("DELETE FROM foods;")
	c0.execute("DELETE FROM collection_infos;")
	c0.execute("UPDATE sqlite_sequence SET seq = 0 where name = 'collection_infos';")
	c0.execute("UPDATE sqlite_sequence SET seq = 0 where name = 'foods';")

def cellNotNone(sheet, xrange, yrange):
	for x in xrange:
		for y in yrange:
			tmp = sheet.cell(x, y).value
			if tmp != "":
				yield tmp

def getQualityDir(xls):
	quality_sheet = xls.sheet_by_name("品质")
	quality_dir = {"紫色":[],"蓝色":[]}
	for purple_thing in cellNotNone(quality_sheet, range(1, quality_sheet.nrows), range(1)):
		quality_dir["紫色"].append(purple_thing)
	for blue_thing in cellNotNone(quality_sheet, range(1, quality_sheet.nrows), range(1, 2)):
		quality_dir["蓝色"].append(blue_thing)
	return quality_dir

def fillCollectionInfos(xls, conn, quality_dir):
	location_sheet = xls.sheet_by_name("地点")
	location = None
	c0 = conn.cursor()
	for x in range(location_sheet.nrows):
		for tmp in cellNotNone(location_sheet, range(x, x + 1), range(1)):
			location = tmp
		# print(location)
		address = None
		for tmp in cellNotNone(location_sheet, range(x, x + 1), range(1, 2)):
			address = tmp
		if not address:
			continue
		for thing in cellNotNone(location_sheet, range(x, x + 1), range(2, location_sheet.ncols)):
			quality = "绿色"
			if thing in quality_dir["紫色"]:
				quality = "紫色"
			elif thing in quality_dir["蓝色"]:
				quality = "蓝色"
			c0.execute("INSERT INTO collection_infos (LOCATION, ADDRESS, THING, QUALITY) values (\"{}\", \"{}\", \"{}\", \"{}\")".format(location, address, thing, quality))

def fillFoods(xls, conn):
	food_sheet = xls.sheet_by_name("食物")
	c0 = conn.cursor()
	pot = None
	for x in range(food_sheet.nrows):
		for tmp in cellNotNone(food_sheet, range(x, x + 1), range(1)):
			pot = tmp
		full = None
		for tmp in cellNotNone(food_sheet, range(x, x + 1), range(1, 2)):
			full = tmp
		if not full:
			continue
		favor = None
		for tmp in cellNotNone(food_sheet, range(x, x + 1), range(2, 3)):
			favor = tmp
		if not favor:
			continue
		addon = None
		for tmp in cellNotNone(food_sheet, range(x, x + 1), range(3, 4)):
			addon = tmp
		if not addon:
			continue
		good_ = None
		for tmp in cellNotNone(food_sheet, range(x, x + 1), range(4, 5)):
			good_ = tmp
		if not good_:
			continue
		goods = good_.split("|")
		name = None
		for tmp in cellNotNone(food_sheet, range(x, x + 1), range(5, 6)):
			name = tmp
		if not name:
			continue
		materials = []
		for material in cellNotNone(food_sheet, range(x, x + 1), range(6, food_sheet.ncols)):
			materials.append(material)
		for good in goods:
			c0.execute("INSERT INTO foods (FULL, FAVOR, POT, ADDON, GOOD, NAME, MATERIALS) values ({}, {}, \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(full, favor, pot, addon, good, name, formatList(materials)))



def sync(xls, conn):
	emptyDB(conn)
	quality_dir = getQualityDir(xls)
	fillCollectionInfos(xls, conn, quality_dir)
	fillFoods(xls, conn)

def main():
	xls = xlrd.open_workbook("collections.xls")
	conn = sqlite3.connect("collections.db")
	sync(xls, conn)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()