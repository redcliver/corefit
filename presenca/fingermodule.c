#include <Python.h>

/*
* Implements an example function.
*/
PyDoc_STRVAR(digitalmodule_example_doc, "example(obj, number)\
\
Example function");

PyObject *digitalmodule_example(PyObject *self, PyObject *args, PyObject *kwargs) {
	/* Shared references that do not need Py_DECREF before returning. */
	PyObject *obj = NULL;
	int number = 0;

	/* Parse positional and keyword arguments */
	static char* keywords[] = { "obj", "number", NULL };
	if (!PyArg_ParseTupleAndKeywords(args, kwargs, "Oi", keywords, &obj, &number)) {
		return NULL;
	}

	/* Function implementation starts here */

	if (number < 0) {
		PyErr_SetObject(PyExc_ValueError, obj);
		return NULL;    /* return NULL indicates error */
	}

	Py_RETURN_NONE;
}

/*
* List of functions to add to digitalmodule in exec_digitalmodule().
*/
static PyMethodDef digitalmodule_functions[] = {
	{ "example", (PyCFunction)digitalmodule_example, METH_VARARGS | METH_KEYWORDS, digitalmodule_example_doc },
{ NULL, NULL, 0, NULL } /* marks end of array */
};

/*
* Initialize digitalmodule. May be called multiple times, so avoid
* using static state.
*/
int exec_digitalmodule(PyObject *module) {
	PyModule_AddFunctions(module, digitalmodule_functions);

	PyModule_AddStringConstant(module, "__author__", "HeadTec");
	PyModule_AddStringConstant(module, "__version__", "1.0.0");
	PyModule_AddIntConstant(module, "year", 2018);

	return 0; /* success */
}

/*
* Documentation for digitalmodule.
*/
PyDoc_STRVAR(digitalmodule_doc, "The digitalmodule module");


static PyModuleDef_Slot digitalmodule_slots[] = {
	{ Py_mod_exec, exec_digitalmodule },
{ 0, NULL }
};

static PyModuleDef digitalmodule_def = {
	PyModuleDef_HEAD_INIT,
	"digitalmodule",
	digitalmodule_doc,
	0,              /* m_size */
	NULL,           /* m_methods */
	digitalmodule_slots,
	NULL,           /* m_traverse */
	NULL,           /* m_clear */
	NULL,           /* m_free */
};

PyMODINIT_FUNC PyInit_digitalmodule() {
	return PyModuleDef_Init(&digitalmodule_def);
}
