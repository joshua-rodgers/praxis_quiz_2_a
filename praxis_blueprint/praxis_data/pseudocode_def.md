## 1. Comments & Placeholders

* **Single-line comments**

  ```pseudocode
  // this is a comment
  ```
* **Placeholders** for missing code or conditions

  ```pseudocode
  /* missing code */
  /* missing condition */
  ```

## 2. Data Types & Literals

* **Primitive types**
  `boolean`, `char`, `double`, `float`, `int`, `short`
* **Composite types**
  `int[]`, `int[][]`, `String`
* **Boolean literals**
  `true`, `false`
* **Null literal**
  `null`
* **String literals**

  ```pseudocode
  "Hello, world"
  ```

## 3. Variables & Assignment

* **Declaration with assignment**

  ```pseudocode
  int x ← 5
  String name ← "Alice"
  ```
* **Assignment operator**
  `←`

## 4. Operators

* **Arithmetic**
  `+`, `-`, `*`, `/`, `^`, `%`
  (Note: `/` is floating-point division unless operands are integers and integer division is specified.)
* **Relational**
  `==`, `≠`, `<`, `≤`, `>`, `≥`
* **Logical**
  `and`, `or`, `not`
* **String concatenation**

  ```pseudocode
  String s ← "foo" + "bar"   // yields "foobar"
  ```

## 5. Output

* **Print statement**

  ```pseudocode
  print <expression>
  ```

  Appends a newline after printing.

## 6. Arrays

* **Declaration & initialization**

  ```pseudocode
  int[] a ← {1, 2, 3}
  int b[0..2] ← {1, 2, 3}
  int[][] c        // two-dimensional array
  ```
* **Indexing & assignment**

  ```pseudocode
  a[0] ← 10
  print a[1]      // prints 2
  ```

## 7. Conditional Statements

* **If-then**

  ```pseudocode
  if ( x > 10 )
      print "big number"
  end if
  ```
* **If-then-else**

  ```pseudocode
  if ( x > 10 )
      print "big number"
  else
      print "small number"
  end if
  ```

## 8. Loops

* **For-loop**

  ```pseudocode
  for ( i ← 0; i < 10; i ← i + 1 )
      print i
  end for
  ```
* **While-loop**

  ```pseudocode
  while ( not done )
      doWork()
  end while
  ```
* **Do-while**

  ```pseudocode
  do
      readInput()
  while ( inputInvalid )
  ```
* **Repeat-until**

  ```pseudocode
  repeat
      process()
  until ( success )
  ```

## 9. Procedures & Functions

* **Function with return type**

  ```pseudocode
  int add(a, b)
      return a + b
  end add
  ```
* **Void procedure**

  ```pseudocode
  void greet(name)
      print "Hello, " + name
  end greet
  ```

## 10. Classes & Object-Oriented Features

* **Class declaration**

  ```pseudocode
  class Person
      private String name
      public int age

      void setName(newName)
          name ← newName
      end setName

      String getName()
          return name
      end getName
  end Person
  ```
* **Inheritance and instantiation**

  ```pseudocode
  class Student extends Person
      private int studentID
  end Student

  Student s ← new Student()
  ```

