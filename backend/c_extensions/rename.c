#define PY_SSIZE_T_CLEAN
#include <python3.6m/Python.h>

#include <ctype.h>
#include <string.h>

#include "to_remove.c"

#define bool char
#define true 1
#define false 0
#define strIndex unsigned char


static PyObject* c_rename_file
(PyObject* self, PyObject* args)
{
    const char* constSongTitle;
    char* subIndexPtr;

    PyArg_ParseTuple(args, "s", &constSongTitle);

    // ALGORITHM FOR STRING REMOVAL

    // name = songTitle.lower()
    strIndex titleLength = strlen(constSongTitle) + 1;
    char name[titleLength];
    char songTitle[titleLength];
    for (strIndex c = 0; c != titleLength; c++)
    {
        name[c] = tolower(constSongTitle[c]);
        songTitle[c] = constSongTitle[c];
    }
    name[titleLength] = '\0';
    songTitle[titleLength] = '\0';


    // remove substings

    // repeat until there is no substring left
    bool noMatch = true;
    do {
        noMatch = true;
        for (strIndex sub = 0; sub < TO_REMOVE_LENGTH; sub++)
        {
            // if substring is not found --> continue on the loop
            if ((subIndexPtr = strstr(name, to_remove[sub])) == NULL)
                continue;

            noMatch = false; // this will make the loop repeat
            
            // get the subIndex of the other string
            strIndex subIndex = subIndexPtr - name;

            // get the end pointer of substring to remove
            strIndex subLength = strlen(to_remove[sub]);
            strIndex subEnd = subIndex + subLength;

            // remove substring from songTitle
            for (; songTitle[subEnd]; ++subEnd)
            {
                songTitle[subIndex] = songTitle[subEnd];
                name[subIndex] = songTitle[subEnd];
                subIndex ++;
            }
            songTitle[subIndex] = '\0';     
            name[subIndex] = '\0';   

        }
    } while (!noMatch);

    // remove one char long substrings (redundant spaces, quotes)
    char previous = 0;
    strIndex nameIndex = 0;
    for (strIndex i = 0; songTitle[i]; i++)
    {
        // if space is redundant --> just continue on the loop
        if (songTitle[i] == ' ')
        {
            if (previous == ' ')
                continue;

            // check if next char is a '.' (file extension) --> remove trailing space
            if (songTitle[i+1] == '.')
                continue;

        }
        // in case of multiple trailing spaces before '.' (file extension)
        else if (songTitle[i] == '.' && previous == ' ')
        {
            name[nameIndex-1] = '.';
            previous = '.';
            continue;
        }

        // remove single quotes and double quotes from song title
        else if (songTitle[i] == '"') continue;
        else if (songTitle[i] == '\'') continue;

            
        
        // copy character
        name[nameIndex] = songTitle[i];
        nameIndex ++;
        
        previous = songTitle[i];
    }
    // finally add the null termination character
    name[nameIndex] = '\0';


    return PyUnicode_FromString(name);

}


static PyMethodDef module_methods[] = 
{
    {"c_rename_file", c_rename_file, METH_VARARGS, "Removes common substrings found in video titles"},
    {NULL}
};


static struct PyModuleDef c_rename =
{
    PyModuleDef_HEAD_INIT,
    "c_rename",
    "Optimized file renames",
    -1,
    module_methods
};


PyMODINIT_FUNC PyInit_c_rename(void) {
    return PyModule_Create(&c_rename);
}
