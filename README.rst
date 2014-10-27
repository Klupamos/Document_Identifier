*******************
Document Identifier
*******************

The Document Identifier package has one public function 'Identify'. It looks through a passed module and attempts to construct objects from the remaining passed arguments.

Basic Use
=========

    >>> import document_identifier as di
    >>> import document_identifier.RealID as RealID
    >>> unknown_document = {'raw_input': "   -\x1eQ\x01%PAGETTYSBURG^SMITH$JOHN^11 WINDERMERE ST$^?                                                                  ;63632208065640=160819340807=?"}
    >>> documents = di.Identify(scope=RealID, **unknown_document)  # return all constructable machine readable travel documents.
    >>> print "\n".join(map(str, documents))

Advanced Use
============

Identify's Keywords
-------------------

scope
*****
``scope`` is either a collection of callable's (class constructors), or a module object with an public __all__ collection of classes.

return_single
*************
``return_single`` is a Boolean flag to specify the return type. It defaults to false. When true, ``Identify`` returns the first constructable object found.  When false it returns a list of all constructable object found.

kwargs
******
Identify takes all remaining arguments and passes them to scope's callables. The sub-modules provided with this package, (MRTD, RealID, etc), all take a generic ``raw_input`` parameter which is then rearranged by each class into what it needs.

Creating a module
=================

The Document Identifier package has a ``DocumentBase`` class which defines the ``__init__`` and a basic ``__str__`` methods. It also has a class level ``Format`` dictionary.

* ``__init__`` should be overridden to convert the ``DocumentBase.__init__`` class attributes into the proper format.
* ``Format`` should be overridden to require the proper passed arguments.

Basic Structure
---------------

``Format`` is a dictionary of RE module regular expression objects. Any key present in ``Format`` will be required by ``DocumentBase.__init__``.

It is ``__init__``'s job to match the passed arguments with ``Formats`` values, and create object attributes from the captured regex groups.

    The captured groups will be of type string, and may need reformatting in any derived classes.

Identifying a Barcode
---------------------

For this example we will create our own module that identifies UPC-A style barcodes.

Lets create a file and import the basics.::

    import re
    from document_identifier import DocumentBase
  
    __all__ = ["UPC_A"]
  
Now lets create a Document that matches and captures only 12 digits.::
  
    class UPC_A(DocumentBase):
      Format = {
        'raw_input': re.compile(r'^(?P<number>\d{12})$'),
      }

UPC-A barcodes have a check digit so let add that logic to the constructor.::
    
    def __init__(self, **kwargs):
        super(UPC_A, self).__init__(**kwargs)
        product = 0
        for num, mul in zip(map(int, self.number[:-1]), [3,1]*6):
            product += num * mul
        product = 10 - (product % 10)
        
        if product != int(self.number[-1])):
            raise ValueError("Invalid check digit")

For a more extensive abuse of inheritance check out the MRTD (Machine Readable Travel Document) module.