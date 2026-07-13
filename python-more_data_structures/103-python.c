#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes_obj;
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes_obj = (PyBytesObject *)p;
    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
    for (i = 0; i < (size + 1 > 10 ? 10 : size + 1); i++)
    {
        printf("%02x ", (unsigned char)string[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *list_obj;
    Py_ssize_t size, allocated, i;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
        return;

    list_obj = (PyListObject *)p;
    size = PyList_Size(p);
    allocated = list_obj->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %ld: %s\n", i, type_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
