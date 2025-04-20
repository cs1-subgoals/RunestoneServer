WrClasses-WE2-P2
----------------------

.. qnum::
   :prefix: Q
   :start: 13

    
.. topic:: Subgoals for Writing a Class 2/4

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
      
      
   6. Create constructor (behavior) that creates initial state of object  

      A. public
      B. Same name as class
      C. No return type
      D. Default - no parameters
      E. Logic - initialize all variables
      F. Repeat as needed, adding parameters 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Classes-WE2-P2

   .. clickablearea:: ca-Classes-WE2-P1-13
      :question: Click on all the attributes of the class (4 of them).
      :iscode:
   
      :click-incorrect:public class Book {:endclick:
         :click-correct:private String title;:endclick:
         :click-correct:private String author;:endclick:
         :click-correct:private String publisher;:endclick:
         :click-correct:private int copyrightDate;:endclick:
         
         :click-incorrect:public Book() {:endclick:
            :click-incorrect:title = "";:endclick:
            :click-incorrect:author = "";:endclick:
            :click-incorrect:publisher = "";:endclick:
            :click-incorrect:copyrightDate = -1;:endclick:
         }
         
         :click-incorrect:public Book(String t, String a, String p, int c) {:endclick:
            :click-incorrect:title = t;:endclick:
            :click-incorrect:author = a;:endclick:
            :click-incorrect:publisher = p;:endclick:
            :click-incorrect:copyrightDate = c;:endclick:
         }
      }
      
   .. clickablearea:: ca-Classes-WE2-P1-14
      :question: Click on the header of the default constructor (1).
      :iscode:
   
      :click-incorrect:public class Book {:endclick:
         :click-incorrect:private String title;:endclick:
         :click-incorrect:private String author;:endclick:
         :click-incorrect:private String publisher;:endclick:
         :click-incorrect:private int copyrightDate;:endclick:
         
         :click-correct:public Book() {:endclick:
            :click-incorrect:title = "";
            author = "";
            publisher = "";
            copyrightDate = -1;:endclick:
         }
         
         :click-incorrect:public Book(String t, String a, String p, int c) {:endclick:
            :click-incorrect:title = t;
            author = a;
            publisher = p;
            copyrightDate = c;:endclick:
         }
      }
      
      
   .. clickablearea:: ca-Classes-WE2-P1-15
      :question: Click on the header of the overloaded constructor (1).
      :iscode:
   
      :click-incorrect:public class Book {:endclick:
         :click-incorrect:private String title;:endclick:
         :click-incorrect:private String author;:endclick:
         :click-incorrect:private String publisher;:endclick:
         :click-incorrect:private int copyrightDate;:endclick:
         
         :click-incorrect:public Book() {:endclick:
            :click-incorrect:title = "";
            author = "";
            publisher = "";
            copyrightDate = -1;:endclick:
         }
         
         :click-correct:public Book(String t, String a, String p, int c) {:endclick:
            :click-incorrect:title = t;
            author = a;
            publisher = p;
            copyrightDate = c;:endclick:
         }
      }
      
      
   .. clickablearea:: ca-Classes-WE2-P1-16
      :question: Click on the overloaded constructor parameters (4).
      :iscode:
   
      :click-incorrect:public class Book {:endclick:
         :click-incorrect:private String title;:endclick:
         :click-incorrect:private String author;:endclick:
         :click-incorrect:private String publisher;:endclick:
         :click-incorrect:private int copyrightDate;:endclick:
         
         :click-incorrect:public Book():endclick: {
            :click-incorrect:title = "";:endclick:
            :click-incorrect:author = "";:endclick:
            :click-incorrect:publisher = "";:endclick:
            :click-incorrect:copyrightDate = -1;:endclick:
         }
         
         :click-incorrect:public Book:endclick:(:click-correct:String t:endclick:, :click-correct:String a:endclick:, :click-correct:String p:endclick:, :click-correct:int c:endclick:) {
            :click-incorrect:title = t;:endclick:
            :click-incorrect:author = a;:endclick:
            :click-incorrect:publisher = p;:endclick:
            :click-incorrect:copyrightDate = c;:endclick:
         }
      }
      
      
   .. clickablearea:: ca-Classes-WE2-P1-17
      :question: Click on the line where the copyrightDate attribute is initialized in the default constructor (1).
      :iscode:
   
      :click-incorrect:public class Book {:endclick:
         :click-incorrect:private String title;:endclick:
         :click-incorrect:private String author;:endclick:
         :click-incorrect:private String publisher;:endclick:
         :click-incorrect:private int copyrightDate;:endclick:
         
         :click-incorrect:public Book() {:endclick:
            :click-incorrect:title = "";:endclick:
            :click-incorrect:author = "";:endclick:
            :click-incorrect:publisher = "";:endclick:
            :click-correct:copyrightDate = -1;:endclick:
         }
         
         :click-incorrect:public Book(String t, String a, String p, int c) {:endclick:
            :click-incorrect:title = t;:endclick:
            :click-incorrect:author = a;:endclick:
            :click-incorrect:publisher = p;:endclick:
            :click-incorrect:copyrightDate = c;:endclick:
         }
      }
      
      
   .. clickablearea:: ca-Classes-WE2-P1-18
      :question: Click on the line where the author attribute is initialized in the overloaded constructor (1).
      :iscode:
   
      :click-incorrect:public class Book {:endclick:
         :click-incorrect:private String title;:endclick:
         :click-incorrect:private String author;:endclick:
         :click-incorrect:private String publisher;:endclick:
         :click-incorrect:private int copyrightDate;:endclick:
         
         :click-incorrect:public Book() {:endclick:
            :click-incorrect:title = "";:endclick:
            :click-incorrect:author = "";:endclick:
            :click-incorrect:publisher = "";:endclick:
            :click-incorrect:copyrightDate = -1;:endclick:
         }
         
         :click-incorrect:public Book(String t, String a, String p, int c) {:endclick:
            :click-incorrect:title = t;:endclick:
            :click-correct:author = a;:endclick:
            :click-incorrect:publisher = p;:endclick:
            :click-incorrect:copyrightDate = c;:endclick:
         }
      }
   
   
.. activecode:: ac-classes-we2-p2
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }