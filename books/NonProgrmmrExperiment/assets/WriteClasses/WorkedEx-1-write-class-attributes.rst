Worked Example: Writing Classes - Attributes
==================================================

.. topic:: Subgoals for Writing a Class 1/4

   1. Name it 


   2. Differentiate class-level (static) vs. instance/object-level variables  


   3. Differentiate class-level (static) vs. instance/object behaviors/methods 
   

   4. Define class variables (static) as needed '
   
      A. Name 
      B. Data Type 
      C. public / private / final 
      
      
   5. Define instance variables (that you want to be interrelated)  

      A. Name 
      B. Data Type 
      C. private 
      

You can watch this video or read through the content below it.

.. youtube:: __z2ZYyC8ZQ
   :divid: video-writeclass-we1
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem: We will be writing a class to represent an instance of time, like a specific time in the day.

For the first part, determine the appropriate attributes (data) to be stored and declare them

   
---------------------------------------------------------------------------------------------------------

.. topic:: SG1: Name it 

   We will call the class TimeType
   

.. topic:: SG2: Differentiate class-level (static) vs. instance/object-level variables  

   class-level (static) data:  one value shared between ALL instances
   instance-level data: each instance has its own copy

   For time, we want all time instances to be in the same format so 
   static data for format, everything else instance
   

.. topic:: SG3: Differentiate class-level (static) vs. instance/object behaviors/methods 

   All methods will be instance level as the format will be fixed an unchangeable


.. topic:: SG4: Define class variables (static) as needed 

   .. code-block:: java
  
      public class TimeType {
      
         public static final boolean FORMAT24 = true;

      } 
      
   Note the use of the ``final`` keyword to define ``FORMAT24`` as a constant, which makes it safe to expose as ``public``. An alternate implementation might choose to make this value mutable, but private, using static methods to ssssssssaccess and alter it.


.. topic:: SG5: Define instance variables (that you want to be interrelated) 
   
   .. code-block:: java
   
      public class TimeType {
      
         //static var
         public static final boolean FORMAT24 = true;
         
         //instance vars
         private int hour;
         private int minute;
         private int second;

      }


   .. figure:: Figures/WC1-Slide8.PNG
      :alt: UML Diagram
      :scale: 50%
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      classes-we1-p1.rst