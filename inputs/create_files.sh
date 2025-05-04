id_array=(1 2 3)
type_array=(key text)
item_array=(a b)
for id in ${id_array[@]}
do
    for type in ${type_array[@]}
    do 
        if [ "$id" -eq 3 ]; then
            touch "${id}_${type}.txt"
        else
            for item in ${item_array[@]}
            do 
            touch "${id}_${item}_${type}.txt"
            done
        fi

    done
done