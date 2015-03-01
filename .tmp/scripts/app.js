var t;

t = 2;

/*!
 *
 *  Web Starter Kit
 *  Copyright 2014 Google Inc. All rights reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *    https://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License
 *
 */
(function () {
  'use strict';

  var querySelector = document.querySelector.bind(document);

  var navdrawerContainer = querySelector('.navdrawer-container');
  var body = document.body;
  var appbarElement = querySelector('.app-bar');
  var menuBtn = querySelector('.menu');
  var main = querySelector('main');

  function closeMenu() {
    body.classList.remove('open');
    appbarElement.classList.remove('open');
    navdrawerContainer.classList.remove('open');
  }

  function toggleMenu() {
    body.classList.toggle('open');
    appbarElement.classList.toggle('open');
    navdrawerContainer.classList.toggle('open');
    navdrawerContainer.classList.add('opened');
  }

  main.addEventListener('click', closeMenu);
  menuBtn.addEventListener('click', toggleMenu);
  navdrawerContainer.addEventListener('click', function (event) {
    if (event.target.nodeName === 'A' || event.target.nodeName === 'LI') {
      closeMenu();
    }
  });
})();

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIm1vZHVsZS5jb2ZmZWUiLCJtYWluLmpzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBLElBQUEsQ0FBQTs7QUFBQSxDQUFBLEdBQUksQ0FBSixDQUFBOztBQ0FBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSIsImZpbGUiOiJhcHAuanMiLCJzb3VyY2VzQ29udGVudCI6WyJ0ID0gMlxyXG4iLCIvKiFcclxuICpcclxuICogIFdlYiBTdGFydGVyIEtpdFxyXG4gKiAgQ29weXJpZ2h0IDIwMTQgR29vZ2xlIEluYy4gQWxsIHJpZ2h0cyByZXNlcnZlZC5cclxuICpcclxuICogIExpY2Vuc2VkIHVuZGVyIHRoZSBBcGFjaGUgTGljZW5zZSwgVmVyc2lvbiAyLjAgKHRoZSBcIkxpY2Vuc2VcIik7XHJcbiAqICB5b3UgbWF5IG5vdCB1c2UgdGhpcyBmaWxlIGV4Y2VwdCBpbiBjb21wbGlhbmNlIHdpdGggdGhlIExpY2Vuc2UuXHJcbiAqICBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXRcclxuICpcclxuICogICAgaHR0cHM6Ly93d3cuYXBhY2hlLm9yZy9saWNlbnNlcy9MSUNFTlNFLTIuMFxyXG4gKlxyXG4gKiAgVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZVxyXG4gKiAgZGlzdHJpYnV0ZWQgdW5kZXIgdGhlIExpY2Vuc2UgaXMgZGlzdHJpYnV0ZWQgb24gYW4gXCJBUyBJU1wiIEJBU0lTLFxyXG4gKiAgV0lUSE9VVCBXQVJSQU5USUVTIE9SIENPTkRJVElPTlMgT0YgQU5ZIEtJTkQsIGVpdGhlciBleHByZXNzIG9yIGltcGxpZWQuXHJcbiAqICBTZWUgdGhlIExpY2Vuc2UgZm9yIHRoZSBzcGVjaWZpYyBsYW5ndWFnZSBnb3Zlcm5pbmcgcGVybWlzc2lvbnMgYW5kXHJcbiAqICBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZVxyXG4gKlxyXG4gKi9cclxuKGZ1bmN0aW9uICgpIHtcclxuICAndXNlIHN0cmljdCc7XHJcblxyXG4gIHZhciBxdWVyeVNlbGVjdG9yID0gZG9jdW1lbnQucXVlcnlTZWxlY3Rvci5iaW5kKGRvY3VtZW50KTtcclxuXHJcbiAgdmFyIG5hdmRyYXdlckNvbnRhaW5lciA9IHF1ZXJ5U2VsZWN0b3IoJy5uYXZkcmF3ZXItY29udGFpbmVyJyk7XHJcbiAgdmFyIGJvZHkgPSBkb2N1bWVudC5ib2R5O1xyXG4gIHZhciBhcHBiYXJFbGVtZW50ID0gcXVlcnlTZWxlY3RvcignLmFwcC1iYXInKTtcclxuICB2YXIgbWVudUJ0biA9IHF1ZXJ5U2VsZWN0b3IoJy5tZW51Jyk7XHJcbiAgdmFyIG1haW4gPSBxdWVyeVNlbGVjdG9yKCdtYWluJyk7XHJcblxyXG4gIGZ1bmN0aW9uIGNsb3NlTWVudSgpIHtcclxuICAgIGJvZHkuY2xhc3NMaXN0LnJlbW92ZSgnb3BlbicpO1xyXG4gICAgYXBwYmFyRWxlbWVudC5jbGFzc0xpc3QucmVtb3ZlKCdvcGVuJyk7XHJcbiAgICBuYXZkcmF3ZXJDb250YWluZXIuY2xhc3NMaXN0LnJlbW92ZSgnb3BlbicpO1xyXG4gIH1cclxuXHJcbiAgZnVuY3Rpb24gdG9nZ2xlTWVudSgpIHtcclxuICAgIGJvZHkuY2xhc3NMaXN0LnRvZ2dsZSgnb3BlbicpO1xyXG4gICAgYXBwYmFyRWxlbWVudC5jbGFzc0xpc3QudG9nZ2xlKCdvcGVuJyk7XHJcbiAgICBuYXZkcmF3ZXJDb250YWluZXIuY2xhc3NMaXN0LnRvZ2dsZSgnb3BlbicpO1xyXG4gICAgbmF2ZHJhd2VyQ29udGFpbmVyLmNsYXNzTGlzdC5hZGQoJ29wZW5lZCcpO1xyXG4gIH1cclxuXHJcbiAgbWFpbi5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIGNsb3NlTWVudSk7XHJcbiAgbWVudUJ0bi5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIHRvZ2dsZU1lbnUpO1xyXG4gIG5hdmRyYXdlckNvbnRhaW5lci5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIGZ1bmN0aW9uIChldmVudCkge1xyXG4gICAgaWYgKGV2ZW50LnRhcmdldC5ub2RlTmFtZSA9PT0gJ0EnIHx8IGV2ZW50LnRhcmdldC5ub2RlTmFtZSA9PT0gJ0xJJykge1xyXG4gICAgICBjbG9zZU1lbnUoKTtcclxuICAgIH1cclxuICB9KTtcclxufSkoKTtcclxuIl0sInNvdXJjZVJvb3QiOiIvc291cmNlLyJ9