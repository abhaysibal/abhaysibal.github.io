import os
def cleanup():
	for root,folders,files in os.walk(os.getcwd()):
		for file in files:
			g = open(os.path.join(os.getcwd(), file), 'r')
			lines = g.readlines()

			# We need to insert only before the "---" token
			dash_count = 0

			for line_pos in xrange(len(lines)):
				if lines[line_pos].startswith("---"):
					if dash_count == 0:
						dash_count += 1
					elif dash_count == 1:
						lines.insert(line_pos,"published: false\n")
						dash_count += 1
					else:
						continue
			f = open(os.path.join(os.getcwd(), file), 'w')
			for line in lines:
				f.write(line)
			f.close()
			g.close()


cleanup()