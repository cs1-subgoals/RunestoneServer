Assessment: Arrays 2
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

.. timed:: assess-arrays-2
   :nofeedback:
   
   
   .. mchoice:: assess-arrays-2-1
      :answer_a: I only
      :answer_b: II only
      :answer_c: III only
      :answer_d: II and III
      :answer_e: I, II, and III
      :correct: e
      
      The following code segments are supposed to find the maximum value in an array of integers. Assuming that the array ``arr`` has been declared and contains valid integer values, which of the following code segments will correctly assign the maximum value in the array to the variable ``max``?
      
      .. figure:: Figures/assess-arrays-2-q1.png
         :alt: answers for Q1
         
         
   .. mchoice:: assess-arrays-2-2
      :answer_a: The largest value in arr occurs only once and is in arr[0].
      :answer_b: The largest value in arr occurs only once and is in arr[arr.length-1].
      :answer_c: The largest value in arr is negative.
      :answer_d: The largest value in arr is 0.
      :answer_e: The largest value in arr occurs more than once.
      :correct: c
      
      The following code is intended to store the largest value in the integer array arr in the variable maxVal. Which of the following best describes the conditions under which the code will not work as intended?
      
      .. code-block:: java
      
         int maxVal = 0;
         for (int val : arr) {
            if (val > maxVal)
               maxVal = val;
         }


   .. mchoice:: assess-arrays-2-3
      :answer_a: I only
      :answer_b: II only
      :answer_c: III only
      :answer_d: I and III only
      :answer_e: II and III only
      :correct: d
      
      The following code is intended to store the sum of all the values in the integer array ``arr`` in the variable ``total``. Which of the following code segments can be used to replace ``/* missing code */`` so that the code works as intended?
      
      .. code-block:: java
      
         int total = 0;
         /* missing code */
         System.out.println(total);
      
      .. figure:: Figures/assess-arrays-2-q3.png
         :alt: answers for Q3
   
   
   .. mchoice:: assess-arrays-2-4
      :answer_a: Prints the maximum value that occurs in the array nums
      :answer_b: Prints the index of the maximum value that occurs in the array nums
      :answer_c: Prints the number of times that the maximum value occurs in the array nums
      :answer_d: Prints the value that occurs most often in the array nums  
      :answer_e: Prints the index of the value that occurs the most often in the array nums
      :correct: e
      
      Assuming that ``nums`` has been declared and initialized as an array of integer values, which of the following best describes what this code does?
      
      .. code-block:: java
      
         int index = 0;
         int count = 0;
         int m = -1;
         for (int outer = 0; outer < nums.length; outer++) {
            count = 0;
            for (int inner = outer + 1; inner < nums.length; inner++) {
               if (nums[outer] == nums[inner])
                  count++;
            }
            if (count > m) {
               index = outer;
               m = count;
            }
         } // end outer for
         System.out.println(index);