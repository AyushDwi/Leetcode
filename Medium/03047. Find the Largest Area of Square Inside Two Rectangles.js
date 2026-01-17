var largestSquareArea = function (leftBottom, rightTop) {
  const n = leftBottom.length;
  const leftBottomRightTop = leftBottom.map((_, k) => [...leftBottom[k], ...rightTop[k]]);
  let maxArea = 0;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      const [left1, bottom1, right1, top1] = leftBottomRightTop[i];
      const [left2, bottom2, right2, top2] = leftBottomRightTop[j];
      const maxLeft = Math.max(left1, left2);
      const maxBottom = Math.max(bottom1, bottom2);
      const minRight = Math.min(right1, right2);
      const minTop = Math.min(top1, top2);
      const side1 = minRight - maxLeft;
      const side2 = minTop - maxBottom;
      const minside = Math.min(side1, side2);
      if (minside > 0) {
        maxArea = Math.max(maxArea, minside * minside);
      }
    }
  }
  return maxArea;
};
