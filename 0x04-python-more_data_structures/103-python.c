#include <stdio.h>
#include <Python.h>


/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p) {
    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_Size(p);
        Py_ssize_t allocated = ((PyListObject *)p)->allocated;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", allocated);

        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject *item = PyList_GetItem(p, i);
            const char *typeName = Py_TYPE(item)->tp_name;

            printf("Element %ld: %s\n", i, typeName);
        }
    } else {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
    }
}

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */

#include <Python.h>

void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("  size: %ld\n", PyBytes_Size(p));
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("  first %ld bytes: ", PyBytes_Size(p) <= 10 ? PyBytes_Size(p) : 10);

        for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; i++) {
            printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
            if (i < 9)
                printf(" ");
        }
        printf("\n");
    } else {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
    }
}

