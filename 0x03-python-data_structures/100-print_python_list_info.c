#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer PyObject input.
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *list_obj;
	PyObject *obj;

	printf("[*] Size of the Python List = %ld\n", Py_List_Size(p));

	list_obj = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list_obj->allocated);

	for (i = 0; i < Py_List_Size(p); i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
