#!/bin/bash
colcon build
ws=$(pwd)
echo $ws
python_version="3.$(cut -d "." -f 2 <<< $(python3 --version))"
echo "python version: $python_version"

rm -r backup
mkdir backup

for d in $ws/src/*/ ; do
    echo -e "\n\n---------------------\n$d"
    if [[ -e $d/CMakeLists.txt ]]; then
        echo "this is C++ package"
        rm -rf $d

    elif [[ -e $d/setup.py ]]; then
        cd $d   # this is absolute path ws/src/pkg
        echo "this is python package"
        if [[ $(cat setup.py | grep "package_name =") ]]; then
            pkg=$(cat setup.py | grep "package_name =")
        else
            pkg=$(cat setup.py | grep "package_name=")
        fi
        echo $pkg
        if [[ $(grep "'" <<< $pkg) ]]; then
            echo "single quote"
            pkg=$(cut -d "'" -f 2 <<< $pkg)
        else
            echo "double quote"
            pkg=$(cut -d '"' -f 2 <<< $pkg)
        fi
        echo $pkg
        rm -r $ws/build/$pkg
        rm -r $ws/install/$pkg
        mkdir -p $ws/install/$pkg/lib/python$python_version/site-packages
        mkdir $ws/backup/$pkg
        rm -r $pkg.tmp
        mkdir $pkg.tmp
        touch $pkg.tmp/__init__.py
# ==============================================================================================================================
        # get package name from setup.py since it might be different from (basename $d)
        cd $pkg     # this is relative path, ws/src/pkg/pkg
        rm compileList.txt
        for f in *.py ; do
            filename=$(basename $f)
            if [[ $filename == __init__.py ]]; then
                continue
            fi
            echo $f
            echo "#cython: language_level=3" > tmp.py
            echo "import aes_decrypt" >> tmp.py
            echo "aes_decrypt.decrypt()" >> tmp.py
            cat $f >> tmp.py
            mv tmp.py src_$f
            # copy all source code to backup location
            cp src_$f $ws/backup/$pkg/src_$f
            # ================== source file is now updated to include decryt and cython tag =======================
            filename=$(cut -d "." -f 1 <<< $filename)  # <file.py> becomes <file>
            echo $filename >> compileList.txt
            # create wrapper with name as $filename.py
            echo "import lib_$filename" > "$filename.py"
            echo "def main():" >> "$filename.py"
            echo "    lib_$filename.main()" >> "$filename.py"
            echo "if __name__ == '__main__':" >> "$filename.py"
            echo "    main()" >> "$filename.py"
        done
        # still in source code directory of package, ws/src/pkg/pkg
        cp $ws/compile.py compile.py
        python3 compile.py build_ext --inplace
        # move .so and use regex to get filename, so can move wrapper as well to tmp folder
        for so in *.so ; do
            # mv $so $d/$pkg.tmp
            mv $so $ws/install/$pkg/lib/python$python_version/site-packages
            echo "================================$so"
            echo $(cut -d "." -f 1 <<< $so | cut -b 5-)
            mv $(cut -d "." -f 1 <<< $so | cut -b 5-).py $d/$pkg.tmp
        done
        # move aes_decrypt.so to site-packages
        cp $ws/$(ls $ws | grep .so) $ws/install/$pkg/lib/python$python_version/site-packages

        cd ..
        # remove everything else
        rm -r $pkg
        mv $pkg.tmp $pkg
    else
        echo "this is not a ROS2 package"
    fi
done

# build
cd $ws
colcon build

# copy all *.so to right location (need to use python version)

echo -e "\n\n---------------------\n"
