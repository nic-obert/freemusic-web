#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <string.h>


static PyObject* c_rename_file
(PyObject* self, PyObject* args)
{
    const char* constSongTitle;

    PyArg_ParseTuple(args, "s", &constSongTitle);

    // ALGORITHM FOR STRING REMOVAL

    unsigned char titleLength = strlen(constSongTitle) + 1;
    char songTitle[titleLength];

    char* subIndex = (char*)songTitle;

    // copy song title
    for (; *constSongTitle != '\0'; ++constSongTitle)
    {
        // ignore quotes (both double and single)
        if (*constSongTitle == '\''
            || *constSongTitle == '"')
            continue;
        
        *subIndex = *constSongTitle;
        ++ subIndex;
    }
    // add null termination character
    *subIndex = '\0';
    subIndex = (char*)songTitle;
    

    // remove text between parenthesis and redundant spaces
    char* copyIndex = subIndex;

    for (; *subIndex != '\0'; ++subIndex)
    {
        if (*subIndex == '(')
        {
            char* endParen;
            // find the index of closing parenthesis
            if ((endParen = strstr(subIndex+1, ")")) == NULL)
                continue;
            
            // set to null character for strstr
            *endParen = '\0';

            // search for "feat " and "ft " substrings
            if (strstr(subIndex+1, "feat ") != NULL
                || strstr(subIndex+1, "ft ") != NULL)
            {
                // restore string integrity
                *endParen = ')';
            }
            else {
                // if "feat " and "ft " are not between parenthesis
                subIndex = endParen + 1;
            }

        }
        else if (*subIndex == '[')
        {
            char* endBrack;
            // find the index of closing square brackets
            if ((endBrack = strstr(subIndex+1, "]")) == NULL)
                continue;
            
            // set to null character for strstr
            *endBrack = '\0';

            // search for "feat " and "ft " substrings
            if (strstr(subIndex+1, "feat ") != NULL
                || strstr(subIndex+1, "ft ") != NULL)
            {
                // restore string integrity
                *endBrack = ']';
            }
            else {
                // if "feat " and "ft " are not between brackets
                subIndex = endBrack + 1;
            }

        }
        // remove redundant spaces
        else if (*subIndex == ' ')
        {
            // ignore space if next character is also a space
            // or if next character is a dot (file extension)
            if (*(subIndex + 1) == ' '
                || *(subIndex + 1) == '.')
                continue;
        }
        

        // finally copy the character if it was not ignored
        *copyIndex = *subIndex;
        ++ copyIndex;
    }
    // finally add null termination character
    *copyIndex = '\0';


    return PyUnicode_FromString(songTitle);

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
