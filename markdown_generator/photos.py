import os
targetPath=os.path.join(os.path.split(os.path.realpath(__file__))[0], '../_albums')
dirPath=os.path.join(os.path.split(os.path.realpath(__file__))[0], '../images')
dirNames=['ID', 'feature', 'group', 'life', 'other', 'work','test1']
dirMap={
    'ID':'证件照',
    'feature':'feature',
    'group':'集体合影',
    'life':'生活照',
    'other':'其他',
    'work':'工作照',
    'test1':'test2'
}
for dirName in dirNames:
    print(dirPath+'/'+dirName)
    for root,d, files in os.walk(dirPath+'/'+dirName):
        print(files)
        md_filename=dirName+'.md'
        md=''
        md += '---\n'
        md += 'title: "'+dirMap[dirName]+'"\n'
        md += 'collection: albums\n'
        md += 'permalink: /album/'+dirName+'\n'
        md += '---\n'

        for file in files:
            md += '<a href="'+file+'"><img src="../keli_photo/'+ dirName + '/' +file+'" height="100"></a>\n'
        
        md_filename = os.path.join(targetPath, md_filename)
        print(md_filename)
        with open(md_filename, 'w') as f:
            f.write(md)



