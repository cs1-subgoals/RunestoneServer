ObjUse-WE4-P1
------------------

.. qnum::
   :prefix: Q
   :start: 11

    
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

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: ObjUse-WE4-P1


   .. clickablearea:: ca-ObjUse-WE4-P1-11
      :question: Click on the method calls of Scanner objects in the following code
      :iscode:

      :click-incorrect:Scanner:endclick: :click-incorrect:input:endclick: = :click-incorrect:new Scanner(System.in);:endclick:
      :click-incorrect:System.out:endclick:.:click-incorrect:print("Enter Your Full Name: "):endclick:;
      :click-incorrect:String:endclick: :click-incorrect:fullName:endclick: = :click-incorrect:input:endclick::click-correct:.nextLine():endclick:;
      :click-incorrect:System.out:endclick:.:click-incorrect:print("Enter Your Course Name: "):endclick:;
      :click-incorrect:String:endclick: :click-incorrect:courseName:endclick: = :click-incorrect:input:endclick::click-correct:.nextLine():endclick:;
      
      
   .. fillintheblank:: fill-ObjUse-WE4-P1-12

      What data type is returned by calling ``nextLine`` for an instance of Scanner? (Reading the code for the previous question may provide a hint for this one!)		

      - :String: Correct
        :x: Incorrect
   
   
   .. parsonsprob:: parsons-ObjUse-WE4-P1-13

      Put these lines of code in the proper order to read in a decimal then an integer.
      -----
      Scanner input = new Scanner (System.in);
      double x = input.nextDouble();
      int y = input.nextInt();
       

.. activecode:: ac-objuse-we4-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }