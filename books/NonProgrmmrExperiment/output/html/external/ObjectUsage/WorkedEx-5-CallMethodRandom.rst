Worked Example: Call a method of Random
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

.. youtube:: dI-D6ZDgcf0
   :divid: video-useobj-we1-call-random
   :align: center

     
.. topic:: Problem Statement

   Given the following code, how do you create a Random integer value?

   .. code-block:: java

      Random rand = new Random();


.. topic:: SG1: Classify method as static method or instance method
    
    We already have an instance of Random with the variable name ``rand``.
   

.. topic:: SG2: Write (instance / class) dot method name and ( )
   
   First, check the API to find a method that does what we want.

   .. figure:: Figures/Call-method-random.png
      :alt: API docs for Random nextInt method
      
   .. code-block:: java
    
      rand.nextInt()

 
.. topic:: SG3: Determine whether parameter(s) are appropriate

   According to the API documentation, the ``nextInt`` method requires 1 parameter, the exclusive upper bound. If we want to generate random values between 0 to 99 (inclusive) then parameter will be 100.
    
   .. code-block:: java
    
      rand.nextInt(100)


.. topic:: SG4: Determine what the method will return (if anything: data type, void, print, change state of object) and where it will be stored (nowhere, somewhere)

   According to the API documentation, the ``nextInt`` method returns an integer, so we need an ``int`` type variable to store the value.

   .. code-block:: java
    
      int value = input.nextInt();


.. topic:: SG5: Evaluate right hand side (RHS) of assignment (if there is one). Value is dependent on method's purpose
    
   We used the API documentation to choose the correct parameter, such that the RHS will return an integer between 0 to 99 (inclusive).

   .. code-block:: java
    
      int value = input.nextInt();
    
    
.. activecode:: ac-objectuse-we5
   :language: java

   import java.util.Random;
   public class main{
      public static void main(String args[]){   
      }
   }
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      objuse-we5-p1.rst