ObjUse-WE1-P1
------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for using objects (creating instances)

   1. Declare variable of appropriate class datatype.

   2. Assign to variable: keyword new, followed by class name, followed by ().

   3. Determine whether parameter(s) are appropriate (API)

      a. Number of parameters

      b. Data types of the parameters

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: ObjUse-WE1-P1

   .. clickablearea:: ca-ObjUse-WE1-P1-1
      :question: Click on the variables (object references) in the following code
      :iscode:

      :click-incorrect:/* reads input from default - keyboard */:endclick:
      :click-incorrect:Scanner:endclick: :click-correct:input:endclick: = :click-incorrect:new Scanner(System.in);:endclick:
      :click-incorrect:/* reads input from InFile stream */:endclick:
      :click-incorrect:Scanner:endclick: :click-correct:foo:endclick: = :click-incorrect:new Scanner(InFile);:endclick:
      
      
   .. clickablearea:: ca-ObjUse-WE1-P1-2
      :question: Click on the class names (but not constructors) in the following code
      :iscode:

      :click-incorrect:/* reads input from default - keyboard */:endclick:
      :click-correct:Scanner:endclick: :click-incorrect:input:endclick: = :click-incorrect:new Scanner(System.in);:endclick:
      :click-incorrect:/* reads input from InFile stream */:endclick:
      :click-correct:Scanner:endclick: :click-incorrect:foo:endclick: = :click-incorrect:new Scanner(InFile);:endclick:
      
      
   .. clickablearea:: ca-ObjUse-WE1-P1-3
      :question: Click on the calls to the Scanner constructor in the following code
      :iscode:

      :click-incorrect:/* reads input from default - keyboard */:endclick:
      :click-incorrect:Scanner:endclick: :click-incorrect:input:endclick: = :click-correct:new Scanner(System.in);:endclick:
      :click-incorrect:/* reads input from InFile stream */:endclick:
      :click-incorrect:Scanner:endclick: :click-incorrect:foo:endclick: = :click-correct:new Scanner(InFile);:endclick:
      
      
   .. clickablearea:: ca-ObjUse-WE1-P1-4
      :question: Click on the parameters which are passed to the Scanner constructor in the following code
      :iscode:

      :click-incorrect:/* reads input from default - keyboard */:endclick:
      :click-incorrect:Scanner:endclick: :click-incorrect:input:endclick: = :click-incorrect:new Scanner:endclick:(:click-correct:System.in:endclick:);
      :click-incorrect:/* reads input from InFile stream */:endclick:
      :click-incorrect:Scanner:endclick: :click-incorrect:foo:endclick: = :click-incorrect:new Scanner:endclick:(:click-correct:InFile:endclick:);
        

.. activecode:: ac-objuse-we1-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }