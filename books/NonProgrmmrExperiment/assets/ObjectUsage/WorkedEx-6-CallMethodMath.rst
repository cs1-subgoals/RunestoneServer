Worked Example: Call a method of Math
==============================================

.. topic:: Subgoals for Calling a Method

   1. Classify method as static method or instance method
      
      a. If static, use the class name

      b. If instance, must have or create an instance 
        
   2. Write (instance / class) dot method name and ( )

   3. Determine whether parameter(s) are appropriate

      a. Number of parameters passed must match method declaration

      b. Data types of parameters passed must match method declaration (or be assignable)
   
   4. Determine what the method will return (if anything: data type, void, print, change state of object) and where it will be stored (nowhere, somewhere)

   5. Evaluate right hand side (RHS) of assignment (if there is one). Value is dependent on method's purpose

      
You can watch this video or read through the content below it.

.. youtube:: 8XmRJYiu4a8
   :divid: video-useobj-we1-call-math
   :align: center

     
.. topic:: Problem Statement 1

   How can you access the value of PI? (Math.PI)


.. topic:: SG1: Classify method as static method or instance method
    
   The value is stored in the Math class, with only static members. 
   

.. topic:: SG2: Write (instance / class) dot method name and ( )
   
   First, check the API to find the constant value we need.
   
   .. figure:: Figures/MathClassConstants.png
      :alt: API docs for Math class constants
        
   .. code-block:: java
    
      Math.PI;

 
.. topic:: SG3: Determine whether parameter(s) are appropriate

    Not used in this example. We are accessing a data member, not calling a method.


.. topic:: SG4: Determine what the method will return (if anything: data type, void, print, change state of object) and where it will be stored (nowhere, somewhere)

   According to the API documentation, the ``PI`` value is a double-precision decimal, so we need a ``double`` type variable to store the value.

   .. code-block:: java
    
      double pi = Math.PI;


.. topic:: SG5: Evaluate right hand side (RHS) of assignment (if there is one). Value is dependent on method's purpose
    
   Notice the lack of parentheses from the previous subgoal's code. We are directly accessing a value stored statically with the Math class, not calling a method. Generally, we would not store a copy of this value into a new variable, but use it directly in an expression (see chapter Evaluating Expressions).

.. topic:: Problem Statement 2

   How can you get the square root of PI? (Math.sqrt)


.. topic:: SG1: Classify method as static method or instance method
    
   When performing math operations, it can be useful to check the Math class API documentation.
   
   .. figure:: Figures/SomeMathClassMethods.png
      :alt: API docs for Math class methods
   
   The sqrt function is a static method of the class Math.
   

.. topic:: SG2: Write (instance / class) dot method name and ( )
   
   .. code-block:: java
    
      Math.sqrt();

 
.. topic:: SG3: Determine whether parameter(s) are appropriate

   In the documentation, we can drill down for more details on the ``sqrt`` function, which describes the 1 ``double`` parameter. We wish to take the square root of pi, which is a double value we know how to access from Problem Statement 1 above.

   .. code-block:: java
    
      Math.sqrt(Math.PI);
        
   Note: You can pass some other numeric types, such as ``int``, and they will be *promoted* to ``double`` if possible. Otherwise you will get an error.

.. topic:: SG4: Determine what the method will return (if anything: data type, void, print, change state of object) and where it will be stored (nowhere, somewhere)

   According to the API documentation, the ``sqrt`` method returns a ``double`` type value, so we need a ``double`` type variable to store the value.

   .. code-block:: java
    
      double value = Math.sqrt(Math.PI);


.. topic:: SG5: Evaluate right hand side (RHS) of assignment (if there is one). Value is dependent on method's purpose
    
   As written in the previous subgoal, the ``sqrt`` method will calculate the square root of our parameter (Math.PI) and return the result. 

    
.. activecode:: ac-objectuse-we6
   :language: java

   public class main{
      public static void main(String args[]){ 
         System.out.println(Math.PI);
         System.out.println(Math.sqrt(Math.PI));
      }
   }
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      objuse-we6-p1.rst