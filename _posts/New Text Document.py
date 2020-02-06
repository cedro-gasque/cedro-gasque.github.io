for i in range(100):
	with open(f'2020-02-06-test-{i}.md', 'w') as f:
		f.write(f'---\nlayout: post\ntitle: blank\nsubtitle: {"a" * i}\n---\n\n#AAAAAAAAAAAAAAAAA')