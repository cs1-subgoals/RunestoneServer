Assessment: Arrays 3
---------------------------------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. timed:: assess-arrays-3
   :nofeedback:
   
   
   .. mchoice:: assess-arrays-3-1
      :answer_a: abcdef
      :answer_b: aabbccddeeff
      :answer_c: abbccddeef
      :answer_d: abcbcdcdedef
      :answer_e: Nothing is printed because an IndexOutOfBoundedsException is thrown.
      :correct: c
      
      Considering the following code segment, what is printed after execution?
      
      .. code-block:: java

         String str = "abcdef";
         for (int k = 0; k < str.length() - 1; k++)
            System.out.print(str.substring(k, k+2);

   
   .. mchoice:: assess-arrays-3-2
      :answer_a: (pos < arr.length) && (arr[pos] != val)
      :answer_b: (arr[pos] != val) && (pos < arr.length)
      :answer_c: (pos < arr.length) || (arr[pos] != val)
      :answer_d: (arr[pos] == val) && (pos < arr.length)
      :answer_e: (pos < arr.length) || (arr[pos] == val)
      :correct: a
      
      The following method is intended to return the index of the first occurrence of the value ``val`` beyond the position ``start`` in the array ``arr``.
      
      .. code-block:: java
    
         // returns index of first occurrence of val in arr after
         // position start; 
         // returns arr.length if val is not found
         public int findNext (int [] arr, int val, int start) {
            int pos = start + 1;
            while ( /* condition */)
               pos++;
            return pos;
         }
         
      For example, the execution of the following code segment should result in the value ``4`` being printed:
      
      .. code-block:: java

         int [] arr = {11, 22, 100, 33, 100, 11, 44, 100};
         System.out.println(findNext(arr, 100, 2));

      Which of the following expressions could be used to replace ``/* condition */`` so that ``findNext`` will work as intended?


   .. mchoice:: assess-arrays-3-3
      :answer_a: I only
      :answer_b: II only
      :answer_c: III only
      :answer_d: I and II only
      :answer_e: II and III only
      :correct: e
      
      The following method is intended to return a String formed by concatenating elements from the parameter ``words``. The elements to be concatenated start with ``startIndex`` and continue through the last element of ``words`` and should appear in reverse order in the resulting string.
      
      .. code-block:: java
    
         // Assume that words.length > 0 and startIndex >= 0
         public String concatWords (String [] words, int startIndex) {
            String result = "";
            /* missing code */
            return result;
         }

      For example, the execution of the following code segment should result in "CarHouseGorilla" being printed.
      
      .. code-block:: java
      
         String [] things = {"Bear", "Apple", "Gorilla", "House", "Car"};
         System.out.println(concatWords(things, 2));

      Which of the following code segments is a correct replacement for  ``/* missing code */`` so that the method will work as intended?
      
      .. figure:: Figures/assess-arrays-3-q3.png
         :alt: answers for Q3
   
   
   .. mchoice:: assess-arrays-3-4
      :answer_a: 0  0  0  0  0  0
      :answer_b: 0  0  0  0  0  6
      :answer_c: 1  2  3  4  5  6 
      :answer_d: 1  2  3  4  5  0  
      :answer_e: No output, an exception is thrown
      :correct: c
      
      Consider the following two methods that occur in the same class. What is printed as a result to the call ``start()``?
      
      .. code-block:: java
    
         public void changeIt (int [] list, int num) {
            list = new int[5];
            num = 0;
            for (int x = 0; x < list.length; x++)
               list[x] = 0;
         }

         public void start() {
            int [] nums = {1, 2, 3, 4, 5};
            int value = 6;
            changeIt(nums, value);
            for (int k = 0; k < nums.length; k++)
               System.out.print(nums[k] + " ");
            System.out.print(value);
         }


   .. mchoice:: assess-arrays-3-5
      :answer_a: 0  0  0  0  0  0 black
      :answer_b: 0  0  0  0  0  6 blackboard
      :answer_c: 1  2  3  4  5  6 black
      :answer_d: 1  2  3  4  5  0 black
      :answer_e: 1  2  3  4  5  6 blackboard
      :correct: e
      
      Consider the following two methods that occur in the same class. What is printed as a result to the call ``start()``?
      
      .. code-block:: java
    
         public void changeAgain (int [] arr, int val, String word) {
            arr = new int[5];
            val = 0;
            word = word.substring(0,5);
            for (int k = 0; k < arr.length; k++)
               arr[k] = 0;
         }

         public void start() {
            int [] nums = {1, 2, 3, 4, 5};
            int value = 6;
            String name = "blackboard";
            changeAgain(nums, value, name);
            for (int x = 0; x < nums.length; x++)
               System.out.print(nums[x] + " ");
            System.out.print(value + " ");
            System.out.print(name);
         }
