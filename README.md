# Psychometric_Test
Programming problem

Psychometric testing is designed to fin job-relevant information about an applicant that the traditional interview process would not uncover. It typically includes a combination of online and personality tests that measure cognitive ability and personality traits.

A company has psychometric scores for n candidates, and it wil only extend job offers to candidates with scores in the inclusive range given by [lowerLimit, upperLimit]. Given the list of scores and a sequence of score ranges, determine how many candidates the company will extend offers to for each range of scores. For example, if the scores are scores = [1,2,2,3,4] and the limits are 2 and 4, then there are 4 candidates, i.e. those with scores [2,2,3,4] that match the conditions.

Build a function called jobOffes such that it must return an array of q integers where the value at each index i denotes the number of candidates in the inclusive range [lowerLimits[i],upperLimits[i]] that the company will extend offers to.
