// Generated by gencpp from file utils/subscribingRequest.msg
// DO NOT EDIT!


#ifndef UTILS_MESSAGE_SUBSCRIBINGREQUEST_H
#define UTILS_MESSAGE_SUBSCRIBINGREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace utils
{
template <class ContainerAllocator>
struct subscribingRequest_
{
  typedef subscribingRequest_<ContainerAllocator> Type;

  subscribingRequest_()
    : subscribing(false)
    , code()
    , topic()  {
    }
  subscribingRequest_(const ContainerAllocator& _alloc)
    : subscribing(false)
    , code(_alloc)
    , topic(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _subscribing_type;
  _subscribing_type subscribing;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _code_type;
  _code_type code;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _topic_type;
  _topic_type topic;





  typedef boost::shared_ptr< ::utils::subscribingRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::utils::subscribingRequest_<ContainerAllocator> const> ConstPtr;

}; // struct subscribingRequest_

typedef ::utils::subscribingRequest_<std::allocator<void> > subscribingRequest;

typedef boost::shared_ptr< ::utils::subscribingRequest > subscribingRequestPtr;
typedef boost::shared_ptr< ::utils::subscribingRequest const> subscribingRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::utils::subscribingRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::utils::subscribingRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::utils::subscribingRequest_<ContainerAllocator1> & lhs, const ::utils::subscribingRequest_<ContainerAllocator2> & rhs)
{
  return lhs.subscribing == rhs.subscribing &&
    lhs.code == rhs.code &&
    lhs.topic == rhs.topic;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::utils::subscribingRequest_<ContainerAllocator1> & lhs, const ::utils::subscribingRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace utils

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::utils::subscribingRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::utils::subscribingRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::utils::subscribingRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::utils::subscribingRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::utils::subscribingRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::utils::subscribingRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::utils::subscribingRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "db710697a2d4a6e07853e803553a1f97";
  }

  static const char* value(const ::utils::subscribingRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xdb710697a2d4a6e0ULL;
  static const uint64_t static_value2 = 0x7853e803553a1f97ULL;
};

template<class ContainerAllocator>
struct DataType< ::utils::subscribingRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "utils/subscribingRequest";
  }

  static const char* value(const ::utils::subscribingRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::utils::subscribingRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool subscribing\n"
"string code\n"
"string topic\n"
;
  }

  static const char* value(const ::utils::subscribingRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::utils::subscribingRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.subscribing);
      stream.next(m.code);
      stream.next(m.topic);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct subscribingRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::utils::subscribingRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::utils::subscribingRequest_<ContainerAllocator>& v)
  {
    s << indent << "subscribing: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.subscribing);
    s << indent << "code: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.code);
    s << indent << "topic: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.topic);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UTILS_MESSAGE_SUBSCRIBINGREQUEST_H
