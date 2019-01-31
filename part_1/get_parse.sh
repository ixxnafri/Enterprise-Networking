

# get all instances with 12.0.1.63

for f in /home/abinade2/cs436/data/readable/updates.20180129.*
do 
    cat $f | grep 12.0.1.63 >> output.txt
done
