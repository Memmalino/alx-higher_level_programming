#include <Python.h>

/**
 * print_python_bytes - function that prints python bytes
 * @p: the pointer to the python object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i;
	const char *str;
	Py_ssize_t size;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		printf("  size: %ld\n", size);

		str = PyBytes_AsString(p);
		printf("  trying string: %s\n", str);

		printf("  first 10 bytes: ");
		for (i = 0; i < size && i < 10; i++)
		{
			printf("%02hhx", str[i]);
			if (i < size - 1 && i < 9)
				printf(" ");
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - function that prints python list object
 * @p: the pointer to the python list object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PySequence_Size(p);
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PySequence_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyList_Check(item))
			print_python_list(item);
		else
			printf("%s\n", Py_TYPE(item)->tp_name);
		Py_DECREF(item);
	}
}


