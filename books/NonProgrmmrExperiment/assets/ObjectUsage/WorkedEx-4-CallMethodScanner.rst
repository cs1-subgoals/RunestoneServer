Worked Example: Call a method of Scanner
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

.. youtube:: 07spenei05M
   :divid: video-useobj-we1-call-scanner
   :align: center

     
.. topic:: Problem Statement

   Given the following code, how do you read in a double variable?

   .. code-block:: java

      Scanner input = new Scanner(System.in);


.. topic:: SG1: Classify method as static method or instance method
    
   We already have an instance of Scanner with the variable name ``input``.
   

.. topic:: SG2: Write (instance / class) dot method name and ( )
   
   First, check the API to find a method that does what we want.
   
   .. figure:: Figures/Create-instance-widget.png
      :alt: API docs for Scanner nextDouble method
      
   .. code-block:: java
    
      input.nextDouble()

 
.. topic:: SG3: Determine whether parameter(s) are appropriate

   No parameters required (again check the API)


.. topic:: SG4: Determine what the method will return (if anything: data type, void, print, change state of object) and where it will be stored (nowhere, somewhere)

   According to the API documentation, the ``nextDouble`` method returns a double, so we need a ``double`` type variable to store the value.

   .. code-block:: java
    
      double value = input.nextDouble();


.. topic:: SG5: Evaluate right hand side (RHS) of assignment (if there is one). Value is dependent on method's purpose
    
   According to the API documentation, the ``nextDouble`` method reads the next value from the input stream and attempts to convert it into a decimal value.

   .. code-block:: java
   
      double value = input.nextDouble();
    
    
.. activecode:: ac-objectuse-we4
   :language: java

   public class main{
      public static void main(String args[]){   
      }
   }
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      objuse-we4-p1.rst