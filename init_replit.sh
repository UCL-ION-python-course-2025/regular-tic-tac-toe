function getDeltaFolder()
{
    find . -name "*delta_*" -type d
}

folder=$(getDeltaFolder)
mv $folder/* $folder/.* .
rm -r $folder/
pip install -r requirements.txt
