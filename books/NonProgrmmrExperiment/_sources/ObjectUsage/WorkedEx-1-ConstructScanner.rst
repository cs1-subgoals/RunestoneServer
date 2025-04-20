Worked Example: Create Instance of Scanner
==============================================

.. topic:: Subgoals for using objects (creating instances)

   1. Declare variable of appropriate class datatype.
    
   2. Assign to variable: keyword new, followed by class name, followed by ().
    
   3. Determine whether parameter(s) are appropriate (API)
    
      a. Number of parameters
        
      b. Data types of the parameters
       
You can watch this video or read through the content below it.

.. youtube:: Gl7pw1MX-U
   :divid: video-useobj-we1-create-scanner
   :align: center
        
.. topic:: SG1: Declare variable of appropriate class datatype.

   In the code block below, the variable name ``sysinScanner`` was selected to better describe what we are going to do with this Scanner, which will become more clear in SG3.
    
   .. code-block:: java
    
      Scanner sysinScanner;
      
.. topic:: SG2: Assign to variable:  keyword new, followed by class name, followed by ().
    
    .. code-block:: java
    
      sysinScanner = new Scanner();
        
.. topic:: SG3: Determine whether parameter(s) are appropriate (API)

   The figure below shows the Java documentation, so we can determine what parameter(s) we need. Most of the ways to construct a Scanner require exactly 1 parameter, an object that represents the source of input data. We'll use the standard system input from the console ``System.in``.

   .. figure:: Figures/Create-Instance-Scanner.png
      :alt: API docs for Scanner constructor
        
.. activecode:: ac-objectuse-we1
   :language: java

   public class main{
      public static void main(String args[]){   
      }
   }
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      objuse-we1-p1.rst