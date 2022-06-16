from pathlib import Path
import shutil
import datetime
from dateutil.relativedelta import relativedelta

receipt_pre = Path.cwd()/'receipt_pre'
receipt = Path.cwd()/'receipt'

files = list(receipt_pre.glob('**/*.UKE'))
for file in files:
	with open(file, encoding='cp932') as f:
		rows = f.readlines()

	num = 0
	for row in rows:
		text_list = row.split(',')
		if text_list[0] == 'IR':
			seikunengetsu = datetime.datetime.strptime(text_list[7], '%Y%m')
			medical_month = seikunengetsu - relativedelta(months=1)
			folder_name = medical_month.strftime('%Y%m')
			if text_list[1] == '1' or text_list[1] == 1:
				kikan = '社保'
			elif text_list[1] == '2' or text_list[1] == 2:
				kikan = '国保'
		elif text_list[0] == 'RE':
			if len(text_list) == 38:
				file_name = 'RECEIPTC'
			elif len(text_list) == 30:
				file_name = 'RECEIPTD'

	file_name = file_name + kikan + '.UKE'
	out_dir = receipt/folder_name
	if not out_dir.exists():
		out_dir.mkdir()

	out_file = out_dir/file_name
	shutil.copy(file, out_file)


