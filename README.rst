leakz
=====

Python API wrapper for `lea.kz <https://lea.kz/>`_

Usage
=====

.. code-block:: python
  
  import leakz

  print(leakz.leaked_mail("test@email.com"))

  print(leakz.password_from_hash("e6e7c0a347468dd5cc73712fa53861cb"))

  print(leakz.hash_from_password("derrick09"))