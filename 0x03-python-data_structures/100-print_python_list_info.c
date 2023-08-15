#include <Python.h>
/**
 ** print_python_list_info - Print some basic info about Python lists
 ** @p: PyObject
 **
 ** Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
	printf("[*] Allocated = %zd\n", list->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
